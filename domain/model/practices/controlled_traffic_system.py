from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class ControlledTrafficSystemEval(Evaluation):
    use_stc: bool
    total_area_stc: bool
    stc_usage_months: bool


@dataclass
class ControlledTrafficSystemPractice(BasePractice):
    use_stc: bool
    total_area_stc: float
    stc_usage_months: int
    evaluation: Optional[ControlledTrafficSystemEval]
