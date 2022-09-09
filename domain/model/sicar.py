from dataclasses import dataclass
from typing import Optional

from .entity import Entity


@dataclass
class Sicar(Entity):
    idf: int
    city_geoid: str
    city_name: str
    description: str
    subject: str
    area_number: float
    geometry: dict


@dataclass
class SicarFarm(Entity):
    farm_code: str
    city_geoid: str
    city_name: str
    state: str
    city: str
    property_type: str
    status: Optional[str]
    condition: Optional[str]
    geometry: dict
