from pymongo.database import Database
from typing import List, Any, Optional

from domain.model import BasePractice, practice_models
from domain.model.practices import PracticeType
from domain.repository import IPracticeRepository, Period


class PracticeRepository(IPracticeRepository):
    def __init__(self, database: Database):
        self._collection = database.get_collection('practices')

    def find(self, filter: dict = {}) -> List[BasePractice]:
        docs = self._collection.find(filter)
        return [self._to_model(doc) for doc in docs]

    def find_by_id(self, _id: str) -> Optional[BasePractice]:
        doc = self._collection.find_one({'_id': _id})
        return self._to_model(doc) if doc else None

    def add(self, practice: BasePractice) -> BasePractice:
        doc = self._to_doc(practice)
        self._collection.insert_one(doc)
        return practice

    def update(self, practice: BasePractice) -> BasePractice:
        doc = self._to_doc(practice)
        self._collection.replace_one({'_id': practice._id}, doc)
        return practice

    def remove(self, _id: str) -> bool:
        result = self._collection.delete_one({'_id': _id})
        return result.deleted_count > 0

    def _to_model(self, doc: dict) -> BasePractice:
        practice_type = PracticeType[doc['practice_type']]
        model = practice_models[practice_type]
        return model(**doc)

    def _to_doc(self, practice: BasePractice) -> dict:
        doc = practice.asdict()
        doc['practice_type'] = practice.practice_type.value
        return doc

    def count(
        self,
        field: str,
        value: Any,
        period: Period = None,
        practice_type: PracticeType = None
    ) -> int:
        filter = {field: value}

        if period:
            start, end = period
            filter['updated_at'] = {'$gte': start, '$lte': end}

        if practice_type:
            filter['practice_type'] = practice_type.name

        return self._collection.count_documents(filter)
