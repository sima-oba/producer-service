from pymongo.database import Database
from typing import List, Optional

from domain.model import Farm, Owner, ImportInfo
from domain.repository import IFarmRepository


class FarmRepository(IFarmRepository):
    def __init__(self, db: Database):
        self._farms = db['farm']
        self._owners = db['owner']
        self._import_info = db['import_info']

    def summary_farms(self, filter: dict) -> List[dict]:
        docs = self._farms.aggregate([
            {'$match': filter},
            {'$unset': 'geometry'}
        ])
        return list(docs)

    def search_farms(self, filter: dict) -> List[Farm]:
        docs = self._farms.find(filter)
        return [Farm.from_dict(doc) for doc in docs]

    def find_farms_by_ids(self, ids: List[str]) -> List[Farm]:
        docs = self._farms.find({'_id': {'$in': ids}})
        return [Farm.from_dict(doc) for doc in docs]

    def add_farm(self, farm: Farm) -> Farm:
        result = self._farms.insert_one(farm.asdict())
        farm._id = result.inserted_id
        return farm

    def update_farm(self, farm: Farm) -> Farm:
        self._farms.replace_one({'_id': farm._id}, farm.asdict())
        return farm

    def find_farm_by_id(self, _id: str) -> Optional[Farm]:
        doc = self._farms.find_one({'_id': _id})
        return Farm.from_dict(doc) if doc else None

    def find_farm_by_code(self, code: str) -> Optional[Farm]:
        doc = self._farms.find_one({'farm_code': code})
        return Farm.from_dict(doc) if doc else None

    def find_owners(self, filter: dict = None) -> List[Owner]:
        docs = self._owners.find(filter)
        return [Owner.from_dict(doc) for doc in docs]

    def find_owner_by_doc(self, doc: str) -> Optional[Owner]:
        doc = self._owners.find_one({'doc': doc})
        return Owner.from_dict(doc) if doc else None

    def find_owner_by_id(self, _id: str) -> Optional[Farm]:
        doc = self._owners.find_one({'_id': _id})
        return Owner.from_dict(doc) if doc else None

    def add_owner(self, owner: Owner) -> Owner:
        result = self._owners.insert_one(owner.asdict())
        owner._id = result.inserted_id
        return owner

    def update_owner(self, owner: Owner) -> Owner:
        self._owners.replace_one({'_id': owner._id}, owner.asdict())
        return owner

    def add_imported_info(self, import_info: ImportInfo) -> ImportInfo:
        result = self._import_info.insert_one(import_info.asdict())
        import_info._id = result.inserted_id
        return import_info

    def find_imported_info(self) -> List[ImportInfo]:
        docs = self._import_info.find()
        return [ImportInfo.from_dict(doc) for doc in docs]
