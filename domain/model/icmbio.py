from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .entity import Entity


@dataclass
class Geopark(Entity):
    imported_id: str
    type: Optional[str]
    name: Optional[str]
    latitude: float
    longitude: float
    state: Optional[str]
    description: Optional[str]
    geometry: dict


@dataclass
class EcoCorridors(Entity):
    imported_id: str
    name: Optional[str]
    geometry: dict


@dataclass
class GeoSites(Entity):
    imported_id: str
    latitude: float
    longitude: float
    name: Optional[str]
    state: Optional[str]
    type: Optional[str]
    description: Optional[str]
    geometry: dict


@dataclass
class IndigenousLand(Entity):
    imported_id: str
    location: Optional[str]
    population: Optional[int]
    groups: Optional[str]
    state: Optional[str]
    city: Optional[str]
    stage: Optional[str]
    status: Optional[str]
    title: Optional[str]
    document: Optional[str]
    date: Optional[datetime]
    extension: Optional[str]
    area_name: Optional[str]
    geometry: dict


@dataclass
class ConservationUnit(Entity):
    imported_id: str
    name: Optional[str]
    category: Optional[str]
    group: Optional[str]
    sphere: Optional[str]
    creation_year: Optional[str]
    quality: Optional[str]
    legal_act: Optional[str]
    last_update: Optional[datetime]
    original_name: Optional[str]
    geometry: dict
