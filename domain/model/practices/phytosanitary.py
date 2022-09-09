from dataclasses import dataclass
from typing import List, Optional

from .base import BasePractice, Evaluation


@dataclass
class PhytosanitaryEval(Evaluation):
    plague_management: bool
    soybean_rust_management: bool
    biotechnology_employed: bool
    pesticides: bool
    uses_agronomic_management: bool
    uses_refuge: bool
    uses_precision_systems: bool
    uses_mip: bool
    uses_mid: bool


@dataclass
class PhytosanitaryPractice(BasePractice):
    plague_management: List[str]
    soybean_rust_management: List[str]
    biotechnology_employed: List[str]
    pesticides: List[str]
    uses_agronomic_management: bool
    uses_refuge: bool
    uses_precision_systems: bool
    uses_mip: bool
    uses_mid: bool
    evaluation: Optional[PhytosanitaryEval]
