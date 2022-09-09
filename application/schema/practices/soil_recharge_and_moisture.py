from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _SoilRechargeAndMoistureEval(EvaluationSchema):
    soil_moisture_management = fields.Boolean(required=True)
    has_agricultural_practices_relationship = fields.Boolean(required=True)


class SoilRechargeAndMoistureSchema(BasePracticeSchema):
    soil_moisture_management = fields.Boolean(required=True)
    has_agricultural_practices_relationship = fields.Boolean(required=True)
    evaluation = fields.Nested(_SoilRechargeAndMoistureEval, missing=None)
