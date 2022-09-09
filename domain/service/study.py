import logging
from typing import List

from domain.model import Study
from domain.exception import EntityNotFoundError
from domain.repository import IStudyRepository


class StudyService:
    def __init__(self, repo: IStudyRepository):
        self._repo = repo
        self._log = logging.getLogger(self.__class__.__name__)

    def search_studies(self, filter: dict) -> List[Study]:
        return self._repo.find(filter)

    def get_study(self, _id: str) -> Study:
        study = self._repo.find_by_id(_id)

        if study is None:
            raise EntityNotFoundError(Study, _id)

        return study

    def save(self, data: dict) -> Study:
        coordinates = data['geometry']['coordinates']
        latitude = coordinates[1]
        longitude = coordinates[0]

        study = self._repo.find_by_coordinates(latitude, longitude)

        if study is None:
            study = self._repo.add(Study.new(data))
            self._log.debug(f'Added study {study._id}')
        else:
            self._repo.update(study.merge(data))
            self._log.debug(f'Updated study {study._id}')

        return study
