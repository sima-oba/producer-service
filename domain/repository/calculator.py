from abc import ABC, abstractmethod
from typing import List, Optional

from domain.model import CalculatorSettings, CalculatorBundle


class ICalculatorRepository(ABC):
    @abstractmethod
    def find_bundle(self, filter: dict = {}) -> List[CalculatorBundle]:
        pass

    @abstractmethod
    def find_bundle_by_id(self, _id: str) -> Optional[CalculatorBundle]:
        pass

    @abstractmethod
    def add_bundle(self, bundle: CalculatorBundle) -> CalculatorBundle:
        pass

    @abstractmethod
    def remove_bundle(self, _id: str):
        pass

    @abstractmethod
    def save_settings(
        self, settings: CalculatorSettings
    ) -> CalculatorSettings:
        pass

    @abstractmethod
    def load_settings(self) -> Optional[CalculatorSettings]:
        pass
