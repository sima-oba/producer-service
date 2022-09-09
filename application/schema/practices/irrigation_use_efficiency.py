from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _IrrigationUseEfficiencyEval(EvaluationSchema):
    has_irrigated_agriculturearea = fields.Boolean(required=True)
    has_flow_meter = fields.Boolean(required=True)
    meter_transmits_telemetric_data = fields.Boolean(required=True)
    use_of_irrigation_systems = fields.Boolean(required=True)
    total_area_of_irrigation_systems = fields.Boolean(required=True)


class IrrigationUseEfficiencySchema(BasePracticeSchema):
    has_irrigated_agriculturearea = fields.Boolean(required=True)
    has_flow_meter = fields.Boolean(required=True)
    meter_transmits_telemetric_data = fields.Boolean(required=True)
    use_of_irrigation_systems = fields.Boolean(required=True)
    total_area_of_irrigation_systems = fields.Float(required=True)
    evaluation = fields.Nested(_IrrigationUseEfficiencyEval, missing=None)
