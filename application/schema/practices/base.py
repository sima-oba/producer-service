from marshmallow import Schema, fields, EXCLUDE
from marshmallow_enum import EnumField

from domain.model import PracticeType


class BasePracticeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    practice_type = EnumField(PracticeType)
    farm_id = fields.String(required=True)


class EvaluationSchema(Schema):
    resp_id = fields.String(required=True)
    resp_name = fields.String(required=True)
    notes = fields.String(missing=None)
