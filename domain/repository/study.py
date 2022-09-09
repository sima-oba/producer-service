from abc import ABC, abstractmethod
from typing import List, Optional

from ..model import Study


class IStudyRepository(ABC):
    @abstractmethod
    def find(self, filter: dict = None) -> List[Study]:
        pass

    @abstractmethod
    def find_by_id(self, _id: str) -> Optional[Study]:
        pass

    @abstractmethod
    def find_by_coordinates(self, lat: float, lng: float) -> Optional[Study]:
        pass

    @abstractmethod
    def add(self, study: Study) -> Study:
        pass

    @abstractmethod
    def update(self, study: Study) -> Optional[Study]:
        pass
