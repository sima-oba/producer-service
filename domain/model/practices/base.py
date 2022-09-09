from dataclasses import dataclass
from typing import Optional

from ..entity import Entity
from .type import PracticeType


@dataclass
class BasePractice(Entity):
    practice_type: PracticeType
    farm_id: str
    owner_doc: str


@dataclass
class Evaluation:
    resp_id: str
    resp_name: str
    notes: Optional[str]
