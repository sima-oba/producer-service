from marshmallow import Schema, fields, post_load


class StudySchema(Schema):
    areas = fields.List(fields.String(), required=True)
    class_sbs = fields.String(missing=None)
    category = fields.String(missing=None)
    title = fields.String(missing=None)
    author = fields.String(missing=None)
    year = fields.String(missing=None)
    institution = fields.String(missing=None)
    geometry = fields.Dict(required=True)


class StudyQuery(Schema):
    areas = fields.String(data_key='area', missing=None)
    category = fields.String(missing=None)
    author = fields.String(missing=None)
    year = fields.String(missing=None)
    institution = fields.String(missing=None)

    @post_load
    def format(self, data: dict, **_):
        data = {k: v for k, v in data.items() if v is not None}
        return data
