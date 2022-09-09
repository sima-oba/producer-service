from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model import City


class ICityRepository(ABC):
    @abstractmethod
    def summary(self) -> List[dict]:
        pass

    @abstractmethod
    def find_all(self, filter: dict) -> List[City]:
        pass

    @abstractmethod
    def find_one(self, filter: dict) -> Optional[City]:
        pass

    @abstractmethod
    def find_by_id(self, _id: str) -> Optional[City]:
        pass

    @abstractmethod
    def add(self, city: City) -> City:
        pass

    @abstractmethod
    def update(self, city: City) -> City:
        pass
