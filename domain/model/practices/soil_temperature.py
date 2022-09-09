from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class SoilTemperatureEval(Evaluation):
    temperature_measurement: bool


@dataclass
class SoilTemperaturePractice(BasePractice):
    temperature_measurement: bool
    evaluation: Optional[SoilTemperatureEval]
