from pymongo.database import Database
from typing import List, Optional

from domain.model import Sicar, SicarFarm
from domain.repository import ISicarRepository, ISicarFarmRepository


class SicarRepository(ISicarRepository):
    def __init__(self, db: Database):
        self._sicar = db['sicar']

    def search(self, filter: dict) -> List[Sicar]:
        docs = self._sicar.find(filter)
        return [Sicar.from_dict(doc) for doc in docs]

    def add(self, sicar: Sicar) -> Sicar:
        result = self._sicar.insert_one(sicar.asdict())
        sicar._id = result.inserted_id
        return sicar

    def update(self, sicar: Sicar) -> Sicar:
        self._sicar.replace_one({'_id': sicar._id}, sicar.asdict())
        return sicar

    def find_by_idf_subject(self, idf: str, subject: str) -> Optional[Sicar]:
        doc = self._sicar.find_one({
            'idf': idf,
            'subject': subject
        })
        
        return Sicar.from_dict(doc) if doc else None


class SicarFarmRepository(ISicarFarmRepository):
    def __init__(self, db: Database) -> None:
        self._coll = db.get_collection('sicar_farms')

    def add(self, farm: SicarFarm):
        self._coll.insert_one(farm.asdict())

    def update(self, farm: SicarFarm):
        self._coll.replace_one({'farm_id': farm._id}, farm.asdict())

    def find_by_code(self, farm_code: str) -> Optional[SicarFarm]:
        doc = self._coll.find_one({'farm_code': farm_code})
        return SicarFarm.from_dict(doc) if doc else None

    def find_by_city(self, city_geoid: str) -> List[SicarFarm]:
        docs = self._coll.find({'city_geoid': city_geoid})
        return [SicarFarm.from_dict(doc) for doc in docs]
