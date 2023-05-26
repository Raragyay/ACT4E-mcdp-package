from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Optional, Type, TypeVar

import yaml

from . import logger
from .structures import (
    CompositeNamedDP,
    Connection,
    DPSeries,
    FinitePoset,
    ModelFunctionality,
    ModelResource,
    NodeFunctionality,
    NodeResource,
    Numbers,
    Poset,
    PosetProduct,
    PrimitiveDP,
    SimpleWrap,
)

loaders = {}

__all__ = [
    "load_repr1",
    "loader_for",
]


def loader_for(classname: str):
    def dc(f):
        if classname in loaders:
            msg = f"Already registered loader for {classname!r}"
            raise ValueError(msg)
        loaders[classname] = f
        return f

    return dc


@loader_for("PosetProduct")
def load_PosetProduct(ob: dict):
    subs = []
    for p in ob["subs"]:
        p = load_repr1(p, Poset)
        subs.append(p)

    return PosetProduct(subs=subs)


def _load_DP_fields(ob: dict) -> dict:
    description = ob["$schema"].get("description", None)
    F = load_repr1(ob["F"], Poset)
    R = load_repr1(ob["R"], Poset)
    fields = dict(description=description, F=F, R=R)

    if "vu" in ob:
        fields["vu"] = load_repr1(ob["vu"], ValueFromPoset)
    if "opspace" in ob:
        fields["opspace"] = load_repr1(ob["opspace"], Poset)
    if "C" in ob:
        fields["opspace"] = load_repr1(ob["C"], Poset)
    if "factor" in ob:
        from fractions import Fraction

        fields["factor"] = Fraction(ob["factor"])
    return fields


@dataclass
class ValueFromPoset:
    value: object
    poset: Poset


@dataclass
class M_Res_MultiplyConstant_DP(PrimitiveDP):
    vu: ValueFromPoset
    opspace: Poset


@dataclass
class M_Fun_MultiplyConstant_DP(PrimitiveDP):
    vu: ValueFromPoset
    opspace: Poset


@dataclass
class M_Res_AddConstant_DP(PrimitiveDP):
    vu: ValueFromPoset
    opspace: Poset


@dataclass
class M_Fun_AddMany_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_Res_AddMany_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class MeetNDualDP(PrimitiveDP):
    opspace: Poset


@dataclass
class JoinNDP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_Fun_MultiplyMany_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_Res_MultiplyMany_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_Ceil_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_FloorFun_DP(PrimitiveDP):
    opspace: Poset


@dataclass
class M_Fun_AddConstant_DP(PrimitiveDP):
    vu: ValueFromPoset
    opspace: Poset


@dataclass
class M_Res_AddConstant_DP(PrimitiveDP):
    vu: ValueFromPoset
    opspace: Poset


@dataclass
class UnitConversion(PrimitiveDP):
    opspace: Poset
    factor: Fraction


@dataclass
class AmbientConversion(PrimitiveDP):
    pass


@loader_for("ValueFromPoset")
def load_ValueFromPoset(ob: dict):
    poset = load_repr1(ob["poset"], Poset)
    value = ob["value"]
    value = poset.parse_yaml_value(value)
    return ValueFromPoset(value=value, poset=poset)


@loader_for("M_Res_MultiplyConstant_DP")
def load_M_Res_MultiplyConstant_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Res_MultiplyConstant_DP(**fields)


@loader_for("M_Fun_MultiplyConstant_DP")
def load_M_Fun_MultiplyConstant_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Fun_MultiplyConstant_DP(**fields)


@loader_for("M_Res_AddConstant_DP")
def load_M_Res_AddConstant_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Res_AddConstant_DP(**fields)


@loader_for("M_Fun_AddMany_DP")
def load_M_Fun_AddMany_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Fun_AddMany_DP(**fields)


@loader_for("M_Res_AddMany_DP")
def load_M_Res_AddMany_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Res_AddMany_DP(**fields)


@loader_for("M_Res_MultiplyMany_DP")
def load_M_Res_MultiplyMany_DP(ob: dict):
    fields = _load_DP_fields(ob)
    return M_Res_MultiplyMany_DP(**fields)


@loader_for("M_Fun_MultiplyMany_DP")
def load_M_Fun_MultiplyMany_DP(ob: dict):
    fields = _load_DP_fields(ob)

    return M_Fun_MultiplyMany_DP(**fields)


@loader_for("M_Ceil_DP")
def load_M_Ceil_DP(ob: dict):
    fields = _load_DP_fields(ob)

    return M_Ceil_DP(**fields)


@loader_for("M_FloorFun_DP")
def load_M_FloorFun_DP(ob: dict):
    fields = _load_DP_fields(ob)

    return M_FloorFun_DP(**fields)


@loader_for("Conversion")
def load_Conversion(ob: dict):
    fields = _load_DP_fields(ob)

    raise NotImplementedError(ob)
    return PrimitiveDP(**fields)


@loader_for("SeriesN")
def load_SeriesN(ob: dict):
    fields = _load_DP_fields(ob)

    subs = []
    for dp in ob["dps"]:
        dp = load_repr1(dp, PrimitiveDP)
        subs.append(dp)

    return DPSeries(**fields, subs=subs)


#
# @loader_for('M_Ceil_DP')
# def load_M_Ceil_DP(ob: dict):
#     F = load_repr1(ob['F'], Poset)
#     R = load_repr1(ob['R'], Poset)
#
#     return PrimitiveDP(F=F, R=R)


@loader_for("M_Fun_AddConstant_DP")
def load_M_Fun_AddConstant_DP(ob: dict):
    fields = _load_DP_fields(ob)

    return M_Fun_AddConstant_DP(**fields)


@loader_for("AmbientConversion")
def load_AmbientConversion(ob: dict):
    fields = _load_DP_fields(ob)

    return AmbientConversion(**fields)


@loader_for("UnitConversion")
def load_UnitConversion(ob: dict):
    fields = _load_DP_fields(ob)

    return UnitConversion(**fields)


@loader_for("JoinNDP")
def load_JoinNDP(ob: dict):
    fields = _load_DP_fields(ob)

    return JoinNDP(**fields)


@loader_for("MeetNDualDP")
def load_MeetNDualDP(ob: dict):
    fields = _load_DP_fields(ob)
    return MeetNDualDP(**fields)


#
# @loader_for('M_Fun_MultiplyConstant_DP')
# def load_M_Fun_MultiplyConstant_DP(ob: dict):
#     F = load_repr1(ob['F'], Poset)
#     R = load_repr1(ob['R'], Poset)
#
#     return PrimitiveDP(F=F, R=R)


@loader_for("CompositeNamedDP")
def load_CompositeNamedDP(ob: dict):
    functionalities = ob["functionalities"]
    resources = ob["resources"]
    loaded_nodes = {}
    nodes = ob["nodes"]
    for k, v in nodes.items():
        node = load_repr1(v)
        loaded_nodes[k] = node
    connections = []

    for c in ob["connections"]:
        source = c["from"]
        target = c["to"]
        if "node" in source:
            source = NodeResource(source["node"], source["node_resource"])
        else:
            source = ModelFunctionality(source["functionality"])

        if "node" in target:
            target = NodeFunctionality(target["node"], target["node_functionality"])
        else:
            target = ModelResource(target["resource"])

        connections.append(Connection(source=source, target=target))

    return CompositeNamedDP(
        functionalities=functionalities, resources=resources, nodes=loaded_nodes, connections=connections
    )


@loader_for("SimpleWrap")
def load_SimpleWrap(ob: dict):
    functionalities = ob["functionalities"]
    resources = ob["resources"]
    dp = load_repr1(ob["dp"], PrimitiveDP)
    return SimpleWrap(functionalities=functionalities, resources=resources, dp=dp)


@loader_for("FinitePoset")
def load_FinitePoset(ob: dict):
    elements = ob["elements"]
    relations = ob["relations"]
    relations = set(tuple(x) for x in relations)
    elements = set(elements)
    return FinitePoset(elements=elements, relations=relations)


@loader_for("Numbers")
def load_Numbers(ob: dict):
    bottom = Decimal(ob["bottom"])
    top = Decimal(ob["top"])
    units = ob.get("units", "")
    step = Decimal(ob.get("step", 0))
    return Numbers(bottom=bottom, top=top, step=step, units=units)


# write the implementation for `loader_for` that allows to  register
# a function for a given class name

X = TypeVar("X")


def load_repr1(data: dict, T: Optional[Type[X]] = None) -> X:
    if "$schema" not in data:
        raise ValueError("Missing $schema")
    schema = data["$schema"]
    title = schema.get("title", None)
    if title not in loaders:
        msg = f"Cannot find loader for {title!r}: known are {list(loaders)}"
        raise ValueError(msg)
    loader = loaders[title]
    try:
        return loader(data)
    except Exception as e:
        datas = yaml.dump(data, allow_unicode=True)
        logger.exception("Error while loading %r\n%s", title, datas, exc_info=e)
        msg = f"Error while loading {title!r}: \n{datas}"
        raise ValueError(msg) from e
