from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _CorrectiveQualityEval(EvaluationSchema):
    product = fields.Boolean(required=True)
    is_density_adequate = fields.Boolean(required=True)
    is_conditioning_adequate = fields.Boolean(required=True)
    has_declared_elements = fields.Boolean(required=True)
    is_contaminated = fields.Boolean(required=True)
    has_logistical_problems = fields.Boolean(required=True)


class CorrectiveQualitySchema(BasePracticeSchema):
    product = fields.String(required=True)
    is_density_adequate = fields.Boolean(required=True)
    is_conditioning_adequate = fields.Boolean(required=True)
    has_declared_elements = fields.Boolean(required=True)
    is_contaminated = fields.Boolean(required=True)
    has_logistical_problems = fields.Boolean(required=True)
    evaluation = fields.Nested(_CorrectiveQualityEval, missing=None)
