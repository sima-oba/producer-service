from dataclasses import dataclass
from typing import Optional, List

from .entity import Entity


@dataclass
class Study(Entity):
    areas: List[str]
    class_sbs: Optional[str]
    category: Optional[str]
    title: Optional[str]
    author: Optional[str]
    year: Optional[str]
    institution: Optional[str]
    geometry: dict
