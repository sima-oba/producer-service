from pymongo.database import Database
from pymongo import ASCENDING
from typing import List, Optional

from domain.model.city import City
from domain.repository import ICityRepository


class CityRepository(ICityRepository):
    def __init__(self, db: Database):
        self._collection = db.get_collection('cities')

    def summary(self) -> List[dict]:
        docs = self._collection.aggregate([{'$unset': 'geometry'}])
        return list(docs)

    def find_all(self, filter: dict = None) -> List[City]:
        docs = self._collection.find(filter).sort('name', ASCENDING)
        return [City.from_dict(doc) for doc in docs]

    def find_one(self, filter: dict) -> Optional[City]:
        doc = self._collection.find_one(filter)
        return City.from_dict(doc) if doc else None

    def find_by_id(self, _id: str) -> Optional[City]:
        doc = self._collection.find_one({'_id': _id})
        return City.from_dict(doc) if doc else None

    def add(self, city: City) -> City:
        self._collection.insert_one(city.asdict())
        return city

    def update(self, city: City) -> Optional[City]:
        result = self._collection.replace_one({'_id': city._id}, city.asdict())
        return city if result.matched_count > 0 else None
