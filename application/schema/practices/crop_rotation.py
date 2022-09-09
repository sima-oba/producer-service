from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _CropRotationEval(EvaluationSchema):
    practice_crop_rotation = fields.Boolean(required=True)
    crops = fields.Boolean(required=True)


class CropRotationSchema(BasePracticeSchema):
    practice_crop_rotation = fields.Boolean(required=True)
    crops = fields.List(fields.String, missing=[])
    evaluation = fields.Nested(_CropRotationEval, missing=None)
