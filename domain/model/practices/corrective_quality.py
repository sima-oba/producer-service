from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class CorrectiveQualityEval(Evaluation):
    product: bool
    is_density_adequate: bool
    is_conditioning_adequate: bool
    has_declared_elements: bool
    is_contaminated: bool
    has_logistical_problems: bool


@dataclass
class CorrectiveQualityPractice(BasePractice):
    product: str
    is_density_adequate: bool
    is_conditioning_adequate: bool
    has_declared_elements: bool
    is_contaminated: bool
    has_logistical_problems: bool
    evaluation: Optional[CorrectiveQualityEval]
