import logging
from typing import List

from domain.helper import PracticeReport
from domain.exception import EntityNotFoundError
from domain.model import Farm, BasePractice, PracticeType, practice_models
from domain.repository import IFarmRepository, IPracticeRepository


class PracticeService:
    def __init__(
        self,
        farm_repo: IFarmRepository,
        practice_repo: IPracticeRepository
    ):
        self._farm_repo = farm_repo
        self._practice_repo = practice_repo
        self._report = PracticeReport(practice_repo)
        self._log = logging.getLogger(self.__class__.__name__)

    def find_all(self, filter: dict) -> List[BasePractice]:
        return self._practice_repo.find(filter)

    def find_by_type(self, _type: PracticeType) -> List[BasePractice]:
        return self._practice_repo.find({'practice_type': _type.name})

    def find_by_id(self, _id: str) -> BasePractice:
        return self._get_practice(_id)

    def add(self, data: dict) -> BasePractice:
        farm = self._get_farm(data['farm_id'])

        data['owner_doc'] = farm.owner_doc
        practice_class = practice_models[data['practice_type']]
        practice = practice_class.new(data)

        self._practice_repo.add(practice)
        self._log.debug(f'Added {practice.practice_type} {practice._id}')

        return practice

    def update(self, data: dict, _id: str) -> BasePractice:
        farm = self._get_farm(data['farm_id'])

        data['owner_doc'] = farm.owner_doc
        practice = self._get_practice(_id)
        practice = practice.merge(data)

        self._practice_repo.update(practice)
        self._log.debug(f'Updated {practice.practice_type} {practice._id}')

        return practice

    def _get_practice(self, _id: str) -> BasePractice:
        practice = self._practice_repo.find_by_id(_id)

        if practice is None:
            raise EntityNotFoundError(BasePractice, _id)

        return practice

    def _get_farm(self, farm_id: str) -> Farm:
        farm = self._farm_repo.find_farm_by_id(farm_id)

        if farm is None:
            raise EntityNotFoundError(Farm, farm_id)

        return farm

    def remove(self, _id: str):
        is_removed = self._practice_repo.remove(_id)

        if not is_removed:
            raise EntityNotFoundError(BasePractice, _id)

    def get_practice_totals(self, filter: dict) -> dict:
        return self._report.get_totals(**filter)

    def get_practice_report(self, filter: dict) -> dict:
        return self._report.get_report(**filter)
