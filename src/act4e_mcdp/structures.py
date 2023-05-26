from dataclasses import dataclass
from decimal import Decimal

from typing import Optional

__all__ = [
    "CompositeNamedDP",
    "Connection",
    "DPSeries",
    "FinitePoset",
    "ModelFunctionality",
    "ModelResource",
    "NodeFunctionality",
    "NodeResource",
    "Numbers",
    "Numbers",
    "Poset",
    "PosetProduct",
    "PrimitiveDP",
    "SimpleWrap",
]


@dataclass
class Poset:
    def parse_yaml_value(self, ob: object) -> object:
        raise NotImplementedError(type(self))


@dataclass
class Numbers(Poset):
    bottom: Decimal
    top: Decimal
    step: Decimal  # if 0 = "continuous"
    units: str  # if empty = dimensionless

    def parse_yaml_value(self, ob: object) -> object:
        if not isinstance(ob, str):
            msg = "Expected string, got %s" % type(ob)
            raise ValueError(msg)
        return Decimal(ob)


@dataclass
class FinitePoset(Poset):
    elements: set[str]
    relations: set[tuple[str, str]]

    def parse_yaml_value(self, ob: object) -> object:
        return ob


@dataclass
class PosetProduct(Poset):
    subs: list[Poset]

    def parse_yaml_value(self, ob: object) -> object:
        if not isinstance(ob, list):
            msg = "Expected list, got %s" % type(ob)
            raise ValueError(msg)
        val = []
        for el, sub in zip(ob, self.subs):
            el = sub.parse_yaml_value(el)
            val.append(el)

        return tuple(val)


@dataclass
class PrimitiveDP:
    description: Optional[str]
    F: Poset
    R: Poset


@dataclass
class DPSeries(PrimitiveDP):
    subs: list[PrimitiveDP]


@dataclass
class NamedDP:
    functionalities: list[str]
    resources: list[str]


@dataclass
class SimpleWrap(NamedDP):
    dp: PrimitiveDP


@dataclass
class NodeResource:
    node: str
    resource: str


@dataclass
class NodeFunctionality:
    node: str
    functionality: str


@dataclass
class ModelFunctionality:
    functionality: str


@dataclass
class ModelResource:
    resource: str


@dataclass
class Connection:
    source: ModelFunctionality | NodeResource
    target: ModelResource | NodeFunctionality


@dataclass
class CompositeNamedDP(NamedDP):
    nodes: dict[str, NamedDP]
    connections: list[Connection]
