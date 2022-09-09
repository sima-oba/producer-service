from dataclasses import dataclass
from .entity import Entity


@dataclass
class ImportInfo(Entity):
    imported_owners: int
    imported_farms: int
