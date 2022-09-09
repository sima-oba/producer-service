from dataclasses import dataclass
from typing import List, Optional

from .base import BasePractice, Evaluation


@dataclass
class CropRotationEval(Evaluation):
    practice_crop_rotation: bool
    crops: bool


@dataclass
class CropRotationPractice(BasePractice):
    practice_crop_rotation: bool
    crops: List[str]
    evaluation: Optional[CropRotationEval]
