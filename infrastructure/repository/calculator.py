from pymongo.database import Database
from typing import Optional, List

from domain.model import (
    CalculatorSettings,
    CalculatorBundle,
)
from domain.repository import ICalculatorRepository


class CalculatorRepository(ICalculatorRepository):
    def __init__(self, db: Database):
        self._calc_bundle = db.get_collection('calculator_bundle')
        self._calc_settings = db.get_collection('calculator_settings')

    def find_bundle(self, filter: dict = {}) -> List[CalculatorBundle]:
        docs = self._calc_bundle.find(filter)
        return [CalculatorBundle.from_dict(doc) for doc in docs]

    def find_bundle_by_id(self, _id: str) -> Optional[CalculatorBundle]:
        doc = self._calc_bundle.find_one({'_id': _id})
        return CalculatorBundle.from_dict(doc) if doc else None

    def add_bundle(self, bundle: CalculatorBundle) -> CalculatorBundle:
        self._calc_bundle.insert_one(bundle.asdict())
        return bundle

    def remove_bundle(self, _id: str):
        self._calc_bundle.delete_one({'_id': _id})

    def save_settings(
        self, settings: CalculatorSettings
    ) -> CalculatorSettings:
        self._calc_settings.replace_one({}, settings.asdict(), upsert=True)
        return settings

    def load_settings(self) -> Optional[CalculatorSettings]:
        doc = self._calc_settings.find_one({'_id': {'$ne': None}})
        return CalculatorSettings.from_dict(doc) if doc else None
