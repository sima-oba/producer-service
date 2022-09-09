from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model import Farm, Owner, ImportInfo


class IFarmRepository(ABC):
    @abstractmethod
    def summary_farms(self, filter: dict) -> List[dict]:
        pass

    @abstractmethod
    def search_farms(self, filter: dict) -> List[Farm]:
        pass

    @abstractmethod
    def find_farms_by_ids(self, id: List[str]) -> List[Farm]:
        pass

    @abstractmethod
    def find_farm_by_id(self, _id: str) -> Optional[Farm]:
        pass

    @abstractmethod
    def find_farm_by_code(self, code: str) -> Optional[Farm]:
        pass

    @abstractmethod
    def add_farm(self, farm: Farm) -> Farm:
        pass

    @abstractmethod
    def update_farm(self, farm: Farm) -> Farm:
        pass

    def find_owners(self, filter: dict = None) -> List[Owner]:
        pass

    @abstractmethod
    def find_owner_by_doc(self, doc: str) -> Optional[Owner]:
        pass

    @abstractmethod
    def find_owner_by_id(self, _id: str) -> Optional[Owner]:
        pass

    @abstractmethod
    def add_owner(self, owner: Owner) -> Owner:
        pass

    @abstractmethod
    def update_owner(self, owner: Owner) -> Owner:
        pass

    @abstractmethod
    def add_imported_info(self, import_info: ImportInfo) -> ImportInfo:
        pass

    @abstractmethod
    def find_imported_info(self) -> List[ImportInfo]:
        pass
