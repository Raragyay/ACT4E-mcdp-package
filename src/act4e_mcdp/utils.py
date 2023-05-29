import argparse
import os
import sys
from importlib import import_module

import yaml

from . import logger
from .primitivedps import PrimitiveDP
from .loading import load_repr1, parse_yaml_value
from .nameddps import NamedDP
from .solution_interface import DPSolverInterface

__all__ = [
    "import_from_string",
]


def import_from_string(dot_path: str) -> object:
    module_path, _, name = dot_path.rpartition(".")
    module = import_module(module_path)
    return getattr(module, name)
