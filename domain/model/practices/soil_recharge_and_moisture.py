from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class SoilRechargeAndMoistureEval(Evaluation):
    soil_moisture_management: bool
    has_agricultural_practices_relationship: bool


@dataclass
class SoilRechargeAndMoisturePractice(BasePractice):
    soil_moisture_management: bool
    has_agricultural_practices_relationship: bool
    evaluation: Optional[SoilRechargeAndMoistureEval]
