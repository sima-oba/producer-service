import logging
from datetime import datetime
from typing import List

from domain.model import Sicar, SicarFarm, City
from domain.exception import EntityNotFoundError
from domain.repository import (
    ISicarRepository,
    ISicarFarmRepository,
    ICityRepository
)


class SicarService:
    def __init__(
        self,
        sicar_repo: ISicarRepository,
        farm_repo: ISicarFarmRepository,
        city_repo: ICityRepository
    ):
        self._sicar_repo = sicar_repo
        self._farm_repo = farm_repo
        self._city_repo = city_repo
        self._log = logging.getLogger(self.__class__.__name__)

    def search_areas(self, filter: dict) -> List[Sicar]:
        return self._sicar_repo.search(filter)

    def save_areas(self, data: List[dict], city_id: str) -> City:
        city = self._get_city(city_id)

        for item in data:
            item['city_geoid'] = city.geoid
            item['city_name'] = city.name
            self._save_area(item)

        now = datetime.utcnow()
        city.sicar_updated_at = now
        city.updated_at = now
        city = self._city_repo.update(city)

        return city

    def _save_area(self, data: dict):
        sicar = self._sicar_repo.find_by_idf_subject(
            data['idf'],
            data['subject']
        )

        if sicar is None:
            sicar = Sicar.new(data)
            sicar = self._sicar_repo.add(sicar)
            self._log.debug(f'Added SICAR area with idf={sicar.idf}')
        else:
            sicar = sicar.merge(data)
            sicar = self._sicar_repo.update(sicar)
            self._log.debug(f'Updated SICAR area with idf={sicar.idf}')

    def search_farms(self, city_geoid: str) -> List[SicarFarm]:
        return self._farm_repo.find_by_city(city_geoid)

    def save_farms(self, data: dict, city_id):
        city = self._get_city(city_id)

        for item in data:
            item['city_geoid'] = city.geoid
            item['city_name'] = city.name
            self._save_farm(item)

    def _save_farm(self, data: dict):
        farm = self._farm_repo.find_by_code(data['farm_code'])

        if farm is None:
            farm = SicarFarm.new(data)
            self._farm_repo.add(farm)
            self._log.debug(f'Added SICAR farm with code {farm.farm_code}')
        else:
            farm = farm.merge(data)
            self._farm_repo.update(farm)
            self._log.debug(f'Updated SICAR farm with code {farm.farm_code}')

    def _get_city(self, city_id: str) -> City:
        city = self._city_repo.find_by_id(city_id)

        if city is None:
            raise EntityNotFoundError(City, city_id)

        return city
