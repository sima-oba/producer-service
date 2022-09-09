from marshmallow import fields

from .base import BasePracticeSchema, EvaluationSchema


class _PhytosanitaryEval(EvaluationSchema):
    plague_management = fields.Boolean(required=True)
    soybean_rust_management = fields.Boolean(required=True)
    biotechnology_employed = fields.Boolean(required=True)
    pesticides = fields.Boolean(required=True)
    uses_agronomic_management = fields.Boolean(required=True)
    uses_refuge = fields.Boolean(required=True)
    uses_precision_systems = fields.Boolean(required=True)
    uses_mip = fields.Boolean(required=True)
    uses_mid = fields.Boolean(required=True)


class PhytosanitarySchema(BasePracticeSchema):
    plague_management = fields.List(fields.String())
    soybean_rust_management = fields.List(fields.String())
    biotechnology_employed = fields.List(fields.String())
    pesticides = fields.List(fields.String())
    uses_agronomic_management = fields.Boolean(required=True)
    uses_refuge = fields.Boolean(required=True)
    uses_precision_systems = fields.Boolean(required=True)
    uses_mip = fields.Boolean(required=True)
    uses_mid = fields.Boolean(required=True)
    evaluation = fields.Nested(_PhytosanitaryEval, missing=None)
