from pymongo.database import Database
from typing import List, Optional

from domain.model import Study
from domain.repository import IStudyRepository


class StudyRepository(IStudyRepository):
    def __init__(self, db: Database):
        self._collection = db.get_collection('studies')

    def find(self, filter: dict = None) -> List[Study]:
        docs = self._collection.find(filter)
        return [Study.from_dict(doc) for doc in docs]

    def find_by_id(self, _id: str) -> Optional[Study]:
        doc = self._collection.find_one({'_id': _id})
        return Study.from_dict(doc) if doc else None

    def find_by_coordinates(self, lat: float, lng: float) -> Optional[Study]:
        doc = self._collection.find_one({
            'geometry.coordinates.0': lng,
            'geometry.coordinates.1': lat
        })

        return Study.from_dict(doc) if doc else None

    def add(self, study: Study) -> Study:
        self._collection.insert_one(study.asdict())
        return study

    def update(self, study: Study) -> Optional[Study]:
        self._collection.replace_one({'_id': study._id}, study.asdict())
        return study
