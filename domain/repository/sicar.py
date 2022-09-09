from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model import Sicar, SicarFarm


class ISicarRepository(ABC):
    @abstractmethod
    def search(self, filter: dict) -> List[Sicar]:
        pass

    @abstractmethod
    def find_by_idf_subject(self, idf: int, subject: str) -> Optional[Sicar]:
        pass

    @abstractmethod
    def add(self, sicar: Sicar) -> Sicar:
        pass

    @abstractmethod
    def update(self, sicar: Sicar) -> Sicar:
        pass


class ISicarFarmRepository(ABC):
    @abstractmethod
    def add(self, farm: SicarFarm):
        pass

    @abstractmethod
    def update(self, farm: SicarFarm):
        pass

    @abstractmethod
    def find_by_code(self, farm_code: str) -> Optional[SicarFarm]:
        pass

    @abstractmethod
    def find_by_city(self, city_geoid: str) -> List[SicarFarm]:
        pass
