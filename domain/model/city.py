from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .entity import Entity


@dataclass
class City(Entity):
    geoid: str
    name: str
    state: str
    geometry: dict
    sicar_updated_at: Optional[datetime]
