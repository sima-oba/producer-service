from abc import ABC, abstractmethod
from typing import List, Optional
from ..model.entity import Entity


class IIcmbioRepository(ABC):

    @abstractmethod
    def find(self, collection: Entity, filter: dict = None) -> List[Entity]:
        pass

    @abstractmethod
    def find_by_imported_id(
        self,
        collection: Entity,
        _id: str
    ) -> Optional[Entity]:
        pass

    @abstractmethod
    def add(self, collection: Entity, consv_unit: Entity) -> Entity:
        pass

    @abstractmethod
    def update(
        self,
        collection: Entity,
        consv_unit: Entity
    ) -> Optional[Entity]:
        pass
