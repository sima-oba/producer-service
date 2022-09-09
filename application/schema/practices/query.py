from marshmallow import Schema, fields, post_load
from marshmallow.validate import OneOf

from domain.model import PracticeType

PRACTICE_VALUES = PracticeType.values()


class PracticeQuery(Schema):
    farm_id = fields.String(missing=None)
    practice_type = fields.String(validate=OneOf(PRACTICE_VALUES))

    @post_load
    def format(self, data: dict, **_):
        return {k: v for k, v in data.items() if v is not None}


class ReportQuery(Schema):
    practice_type = fields.String(validate=OneOf(PRACTICE_VALUES))
    start = fields.DateTime()
    end = fields.DateTime()
