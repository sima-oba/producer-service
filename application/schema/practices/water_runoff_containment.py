from marshmallow import fields, validate

from .base import BasePracticeSchema, EvaluationSchema


class _WaterRunoffContainmentEval(EvaluationSchema):
    has_micro_dams = fields.Boolean(required=True)
    micro_dams_quality = fields.Boolean(required=True)
    has_level_curves = fields.Boolean(required=True)
    level_curves_convergent_with_neighbors = fields.Boolean(required=True)
    level_curves_quality = fields.Boolean(required=True)


class WaterRunoffContainmentSchema(BasePracticeSchema):
    has_micro_dams = fields.Boolean(required=True)
    micro_dams_quality = fields.Integer(
        validate=validate.Range(min=0, max=3),
        required=True
    )
    has_level_curves = fields.Boolean(required=True)
    level_curves_convergent_with_neighbors = fields.Boolean(required=True)
    level_curves_quality = fields.Integer(
        validate=validate.Range(min=0, max=3),
        required=True
    )
    evaluation = fields.Nested(_WaterRunoffContainmentEval, missing=None)
