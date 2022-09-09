from dataclasses import dataclass
from typing import Optional

from .base import BasePractice, Evaluation


@dataclass
class IrrigationUseEfficiencyEval(Evaluation):
    has_irrigated_agriculturearea: bool
    has_flow_meter: bool
    meter_transmits_telemetric_data: bool
    use_of_irrigation_systems: bool
    total_area_of_irrigation_systems: bool


@dataclass
class IrrigationUseEfficiencyPractice(BasePractice):
    has_irrigated_agriculturearea: bool
    has_flow_meter: bool
    meter_transmits_telemetric_data: bool
    use_of_irrigation_systems: bool
    total_area_of_irrigation_systems: float
    evaluation: Optional[IrrigationUseEfficiencyEval]
