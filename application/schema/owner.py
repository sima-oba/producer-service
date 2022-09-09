from marshmallow import Schema, fields


class OwnerSchema(Schema):
    doc = fields.String(required=True)
    name = fields.String(required=True)
    email = fields.String(missing=True)
    phone = fields.String(missing=None)
    defaulting = fields.Boolean(required=True)
