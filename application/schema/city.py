from marshmallow import Schema, fields


class CitySchema(Schema):
    geoid = fields.String(required=True)
    name = fields.String(required=True)
    state = fields.String(required=True)
    geometry = fields.Dict(required=True)
