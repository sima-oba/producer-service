import logging
from uuid import uuid4
from datetime import datetime
from typing import List, Optional

from domain.exception import EntityNotFoundError, InvalidStateError
from domain.repository import ICalculatorRepository, IFarmRepository
from domain.model import (
    Farm,
    CalculatorSettings,
    CalculatorDataCollect,
    CalculatorBundle
)
from ..helper import CalculatorHelper


class CarbonCalculatorService:
    def __init__(
        self,
        calc_repo: ICalculatorRepository,
        farm_repo: IFarmRepository
    ):
        self._calc_repo = calc_repo
        self._farm_repo = farm_repo
        self._log = logging.getLogger(__name__)

    def get_all(self, filter: dict = None) -> List[CalculatorBundle]:
        return self._calc_repo.find_bundle(filter)

    def get_by_id(self, _id: str) -> CalculatorBundle:
        bundle = self._calc_repo.find_bundle_by_id(_id)

        if bundle is None:
            raise EntityNotFoundError(CalculatorBundle, _id)

        return bundle

    def get_by_producer(self, producer_id: str) -> CalculatorBundle:
        bundle = self._calc_repo.find_bundle({'producer_id': producer_id})

        if bundle is None:
            raise EntityNotFoundError(CalculatorBundle, producer_id)

        return bundle

    def calculate(self, data: dict) -> CalculatorBundle:
        farm = self._farm_repo.find_farm_by_id(data['farm_id'])

        if farm is None:
            raise EntityNotFoundError(Farm, data['farm_id'])

        settings = self.load_settings()

        if settings is None:
            raise InvalidStateError('Calculator has not been configured')

        data['farm_name'] = farm.farm_name
        data_collect = CalculatorDataCollect(**data)
        result = CalculatorHelper(settings, data_collect).calculate()
        bundle = CalculatorBundle(
            _id=str(uuid4()),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            owner_doc=farm.owner_doc,
            data_collect=data_collect,
            result=result
        )

        self._calc_repo.add_bundle(bundle)
        self._log.debug(f'Added calculator bundle {bundle._id}')

        return bundle

    def save_settings(self, data: dict) -> CalculatorSettings:
        settings = self._calc_repo.load_settings()

        if settings is None:
            settings = CalculatorSettings.new(data)
        else:
            settings = settings.merge(data)

        self._calc_repo.save_settings(settings)
        self._log.debug('Saved calculator settings')

        return settings

    def remove_by_id(self, _id: str):
        bundle = self.get_by_id(_id)
        self._calc_repo.remove_bundle(bundle._id)

    def load_settings(self) -> Optional[CalculatorSettings]:
        return self._calc_repo.load_settings()

    def set_up_settings(self):
        settings = self._calc_repo.load_settings()

        if settings is not None:
            return

        settings = CalculatorSettings.create_default()
        self._calc_repo.save_settings(settings)
        self._log.debug('Initalized default calculator settings')
