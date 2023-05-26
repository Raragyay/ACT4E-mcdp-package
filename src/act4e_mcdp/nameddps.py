from dataclasses import dataclass

from .posets import Poset
from .primitivedps import PrimitiveDP

__all__ = [
    "CompositeNamedDP",
    "Connection",
    "ModelFunctionality",
    "ModelResource",
    "NamedDP",
    "NodeFunctionality",
    "NodeResource",
    "SimpleWrap",
]


@dataclass
class NamedDP:
    functionalities: dict[str, Poset]
    resources: dict[str, Poset]


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
