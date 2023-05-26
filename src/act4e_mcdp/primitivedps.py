from dataclasses import dataclass
from fractions import Fraction
from typing import Optional

from .posets import Poset

__all__ = [
    "AmbientConversion",
    "DPSeries",
    "JoinNDP",
    "M_Ceil_DP",
    "M_FloorFun_DP",
    "M_Fun_AddConstant_DP",
    "M_Fun_AddMany_DP",
    "M_Fun_MultiplyConstant_DP",
    "M_Fun_MultiplyMany_DP",
    "M_Fun_MultiplyMany_DP",
    "M_Res_AddConstant_DP",
    "M_Res_AddMany_DP",
    "M_Res_MultiplyConstant_DP",
    "M_Res_MultiplyMany_DP",
    "MeetNDualDP",
    "MeetNDualDP",
    "PrimitiveDP",
    "UnitConversion",
    "ValueFromPoset",
]


@dataclass
class PrimitiveDP:
    """
    A generic PrimitiveDP; a morphism of the category DP.

    Other classes derive from this.

    Attributes:
        description: An optional string description.
        F: The functionality poset
        R: The resources poset
    """

    description: Optional[str]
    F: Poset
    R: Poset


@dataclass
class DPSeries(PrimitiveDP):
    """
    A series composition of two or more DPs.

    Attributes:
       subs: The list of DPs

    """

    subs: list[PrimitiveDP]


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
    """
    A unit conversion between real numbers
    given by a factor F (a fraction).

    Relation:

        $$
          \\fun \cdot \\text{factor} \\leq \\res
        $$


    Attributes:
        factor: The fraction F

    """

    opspace: Poset
    factor: Fraction


@dataclass
class AmbientConversion(PrimitiveDP):
    """
    A "conversion" between two posets that are subposets of a common ambient poset.

    Relation:

        $$
          \\fun \\leq_{C}  \\res
        $$

        where $C$ is the common ambient poset.

    Attributes:
        common: The common ambient poset

    """

    common: Poset
