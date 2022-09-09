from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Any, Tuple, Optional

from domain.model.practices import BasePractice, PracticeType

Period = Tuple[datetime, datetime]


class IPracticeRepository(ABC):
    @abstractmethod
    def find(self, filter: dict = None) -> List[BasePractice]:
        pass

    @abstractmethod
    def find_by_id(self, _id: str) -> Optional[BasePractice]:
        pass

    @abstractmethod
    def add(self, practice: BasePractice) -> BasePractice:
        pass

    @abstractmethod
    def update(self, practice: BasePractice) -> BasePractice:
        pass

    @abstractmethod
    def remove(self, _id: str) -> bool:
        pass

    @abstractmethod
    def count(
        self,
        field: str,
        value: Any,
        period: Period = None,
        practice_type: PracticeType = None
    ):
        pass
