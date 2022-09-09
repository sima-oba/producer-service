from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class WaterRunoffContainmentEval(Evaluation):
    has_micro_dams: bool
    micro_dams_quality: bool
    has_level_curves: bool
    level_curves_convergent_with_neighbors: bool
    level_curves_quality: bool


@dataclass
class WaterRunoffContainmentPractice(BasePractice):
    has_micro_dams: bool
    micro_dams_quality: int
    has_level_curves: bool
    level_curves_convergent_with_neighbors: bool
    level_curves_quality: int
    evaluation: Optional[WaterRunoffContainmentEval]
