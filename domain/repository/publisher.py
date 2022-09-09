from abc import ABC, abstractmethod
from typing import Optional


class IPublisher(ABC):
    @abstractmethod
    def send(self, topic: str, data: any, key: Optional[str]) -> str:
        pass
