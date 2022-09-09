from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _SoilTemperatureEval(EvaluationSchema):
    temperature_measurement = fields.Boolean(required=True)


class SoilTemperatureSchema(BasePracticeSchema):
    temperature_measurement = fields.Boolean(required=True)
    evaluation = fields.Nested(_SoilTemperatureEval, missing=None)
