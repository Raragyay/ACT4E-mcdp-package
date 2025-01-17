import argparse
import os
import sys
from typing import Any

import yaml

from . import logger
from .loading import load_repr1, parse_yaml_value
from .nameddps import NamedDP
from .primitivedps import PrimitiveDP
from .solution_interface import DPSolverInterface
from .utils import import_from_string

__all__ = [
    "solve_dp_main",
]


def solve_dp_main() -> None:
    queries = ["FixFunMinRes", "FixResMaxFun"]
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", help="DP Model source (file or URL)", required=True)
    parser.add_argument("--query", help="query", default="FixFunMinRes", required=False)
    parser.add_argument("--data", help="data (YAML Format)", required=True)
    parser.add_argument("--solver", help="Model source (file or URL)", required=True)

    args = parser.parse_args()

    model_source = args.model
    try:
        solver0 = import_from_string(args.solver)
    except Exception as e:
        logger.error("Could not import solver %r", args.solver, exc_info=e)
        sys.exit(1)

    solver: DPSolverInterface

    if isinstance(solver0, DPSolverInterface):
        solver = solver0
    else:
        # noinspection PyCallingNonCallable
        solver = solver0()  # type: ignore
    if not isinstance(solver, DPSolverInterface):
        msg = f"Expected a DPSolverInterface, got {solver!r}"
        raise ValueError(msg)

    query = args.query

    if query not in queries:
        logger.error("Unknown query %r. Known: %r", query, queries)
        sys.exit(1)

    query_data = args.data
    if model_source.startswith("http"):
        import requests

        r = requests.get(model_source)
        if r.status_code != 200:
            logger.error("Cannot download model from %r", model_source)
            sys.exit(1)

        model_source = r.text
        data = yaml.load(model_source, Loader=yaml.SafeLoader)
    else:
        if os.path.exists(model_source):
            model_source = open(model_source, encoding="utf-8").read()
            data = yaml.load(model_source, Loader=yaml.SafeLoader)
        else:
            logger.error("Cannot open file: %r", model_source)
            sys.exit(1)

    model: PrimitiveDP[Any, Any] = load_repr1(data, PrimitiveDP)
    if not isinstance(model, PrimitiveDP):  # type: ignore
        if isinstance(model, NamedDP):
            msg = f"Expected a PrimitiveDP, not a NamedDP. Did you mean to use 'act4e-mcdp-solve-mcdp'?"
            raise ValueError(msg)

        msg = f"Expected a NamedDP, got {model!r}"
        raise ValueError(msg)
    logger.info("model: %s", model)

    yaml_query = yaml.load(query_data, Loader=yaml.SafeLoader)

    if query == "FixFunMinRes":
        value = parse_yaml_value(model.F, yaml_query)

        logger.info("query: %s", value)

        solution = solver.solve_dp_FixFunMinRes(model, value)

        logger.info("solution: %s", solution)

    elif query == "FixResMaxFun":
        value = parse_yaml_value(model.R, yaml_query)

        logger.info("query: %s", value)

        solution = solver.solve_dp_FixFunMinRes(model, value)

        logger.info("solution: %s", solution)

    else:
        raise ValueError(f"Unknown query {query}")
