from typing import Dict

from .base import BasePractice
from .type import PracticeType
from .controlled_traffic_system import ControlledTrafficSystemPractice
from .corrective_quality import CorrectiveQualityPractice
from .crop_rotation import CropRotationPractice
from .irrigation_use_efficiency import IrrigationUseEfficiencyPractice
from .phytosanitary import PhytosanitaryPractice
from .soil_recharge_and_moisture import SoilRechargeAndMoisturePractice
from .soil_temperature import SoilTemperaturePractice
from .sustainable import SustainablePractice
from .water_runoff_containment import WaterRunoffContainmentPractice

__all__ = ['BasePractice', 'PracticeType']

practice_models: Dict[PracticeType, BasePractice] = {
    PracticeType.CONTROLLED_TRAFFIC_SYSTEM: ControlledTrafficSystemPractice,
    PracticeType.CORRECTIVE_QUALITY: CorrectiveQualityPractice,
    PracticeType.CROP_ROTATION: CropRotationPractice,
    PracticeType.IRRIGATION_USE_EFFICIENCY: IrrigationUseEfficiencyPractice,
    PracticeType.PHYTOSANITARY: PhytosanitaryPractice,
    PracticeType.SOIL_RECHARGE_AND_MOISTURE: SoilRechargeAndMoisturePractice,
    PracticeType.SOIL_TEMPERATURE: SoilTemperaturePractice,
    PracticeType.SUSTAINABLE: SustainablePractice,
    PracticeType.WATER_RUNOFF_CONTAINMENT: WaterRunoffContainmentPractice,
}
