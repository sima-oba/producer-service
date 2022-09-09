from dataclasses import dataclass

from .entity import Entity


@dataclass
class Owner(Entity):
    doc: str
    name: str
