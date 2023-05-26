from dataclasses import dataclass
from decimal import Decimal

__all__ = [
    "Numbers",

    "CompositeNamedDP", "Connection", "PrimitiveDP", "DPSeries", "FinitePoset", "ModelFunctionality",
    "ModelResource",
    "NodeFunctionality",
    "NodeResource", 'Numbers',
    "Poset",
    "PosetProduct", "SimpleWrap",

]

from typing import Optional


@dataclass
class Poset:
    pass


@dataclass
class Numbers(Poset):
    bottom: Decimal
    top: Decimal
    step: Decimal  # if 0 = "continuous"
    units: str  # if empty = dimensionless


@dataclass
class FinitePoset(Poset):
    elements: set[str]
    relations: set[tuple[str, str]]


@dataclass
class PosetProduct(Poset):
    subs: list[Poset]


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
