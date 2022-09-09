from dataclasses import dataclass

from .entity import Entity
from .calculator_data_collect import CalculatorDataCollect
from .calculator_result import CalculatorResult


@dataclass
class CalculatorBundle(Entity):
    owner_doc: str
    data_collect: CalculatorDataCollect
    result: CalculatorResult
