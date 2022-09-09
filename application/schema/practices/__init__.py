from .controlled_traffic_system import ControlledTrafficSystemSchema
from .corrective_quality import CorrectiveQualitySchema
from .crop_rotation import CropRotationSchema
from .irrigation_use_efficiency import IrrigationUseEfficiencySchema
from .phytosanitary import PhytosanitarySchema
from .soil_recharge_and_moisture import SoilRechargeAndMoistureSchema
from .soil_temperature import SoilTemperatureSchema
from .sustainable import SustainableSchema
from .water_runoff_containment import WaterRunoffContainmentSchema
from .query import PracticeQuery, ReportQuery

__all__ = [
    'ControlledTrafficSystemSchema',
    'CorrectiveQualitySchema',
    'CropRotationSchema',
    'IrrigationUseEfficiencySchema',
    'PhytosanitarySchema',
    'SoilRechargeAndMoistureSchema',
    'SoilTemperatureSchema',
    'SustainableSchema',
    'WaterRunoffContainmentSchema',
    'PracticeQuery',
    'ReportQuery'
]
