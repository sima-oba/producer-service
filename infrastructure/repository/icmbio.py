from pymongo.database import Database
from typing import List, Optional
from domain.model import (
    Geopark,
    EcoCorridors,
    GeoSites,
    IndigenousLand,
    ConservationUnit
)
from domain.model.entity import Entity
from domain.repository import IIcmbioRepository


class IcmbioRepository(IIcmbioRepository):
    def __init__(self, db: Database):
        self._collections = {
            Geopark: db.get_collection('geopark'),
            EcoCorridors: db.get_collection('ecocorridors'),
            GeoSites: db.get_collection('geosites'),
            IndigenousLand: db.get_collection('indigenousland'),
            ConservationUnit: db.get_collection('conservation_unit')
        }

        self._collections[ConservationUnit].create_index('category')
        self._collections[ConservationUnit].create_index('sphere')

    def find(self, collection: Entity, filter: dict = None) -> List[Entity]:
        docs = self._collections[collection].find(filter)
        return [collection.from_dict(doc) for doc in docs]

    def find_by_imported_id(
        self,
        collection: Entity,
        _id: str
    ) -> Optional[Entity]:
        doc = self._collections[collection].find_one({'imported_id': _id})
        return collection.from_dict(doc) if doc else None

    def add(self, collection: Entity, consv_unit: Entity) -> Entity:
        self._collections[collection].insert_one(consv_unit.asdict())
        return consv_unit

    def update(
        self,
        collection: Entity,
        consv_unit: Entity
    ) -> Optional[Entity]:
        self._collections[collection].replace_one({
            '_id': consv_unit._id}, consv_unit.asdict()
        )
        return consv_unit
