import logging
from typing import List

from domain.model.city import City
from domain.repository import ICityRepository


class CityService:
    def __init__(self, repo: ICityRepository):
        self._repo = repo
        self._log = logging.getLogger(self.__class__.__name__)

    def summary(self) -> List[dict]:
        return self._repo.summary()

    def get_all(self) -> List[City]:
        return self._repo.find_all()

    def save(self, data: dict) -> City:
        city = self._repo.find_one({'geoid': data['geoid']})

        if city:
            city = self._repo.update(city.merge(data))
            self._log.debug(f'updated city {city._id}')
        else:
            city = self._repo.add(City.new(data))
            self._log.debug(f'added city {city._id}')

        return city
