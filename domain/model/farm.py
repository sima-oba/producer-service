from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .entity import Entity


@dataclass
class Farm(Entity):
    owner_doc: str
    farm_code: str
    farm_name: str
    city: str
    state: str
    latitude: float
    longitude: float
    property_type: str
    area: float
    signature_date: datetime
    geometry: dict
    nucleos: Optional[str]
    crops: Optional[List[str]]
    open_areas: Optional[float]
    productive_areas: Optional[float]
    vegetation_types: Optional[List[str]]
    industries: Optional[List[str]]
    aerodrome_lat: Optional[float]
    aerodrome_lng: Optional[float]
