from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _ControlledTrafficSystemEval(EvaluationSchema):
    use_stc = fields.Boolean(required=True)
    total_area_stc = fields.Boolean(required=True)
    stc_usage_months = fields.Boolean(required=True)


class ControlledTrafficSystemSchema(BasePracticeSchema):
    use_stc = fields.Boolean(required=True)
    total_area_stc = fields.Float(required=True)
    stc_usage_months = fields.Integer(required=True)
    evaluation = fields.Nested(_ControlledTrafficSystemEval, missing=None)
