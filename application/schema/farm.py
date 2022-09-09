from marshmallow import Schema, fields, EXCLUDE, post_load


class FarmSchema(Schema):
    owner_doc = fields.String(required=True)
    farm_code = fields.String(required=True)
    farm_name = fields.String(required=True)
    state = fields.String(required=True)
    city = fields.String(required=True)
    property_type = fields.String(required=True)
    area = fields.Float(required=True)
    signature_date = fields.DateTime(format='%Y-%m-%d', required=True)
    geometry = fields.Dict(required=True)

    @post_load
    def format(self, data: dict, **_):
        if isinstance(data['geometry']['coordinates'][0][0][1], float):
            data['latitude'] = data['geometry']['coordinates'][0][0][1]
            data['longitude'] = data['geometry']['coordinates'][0][0][0]
        else:
            data['latitude'] = data['geometry']['coordinates'][0][0][0][1]
            data['longitude'] = data['geometry']['coordinates'][0][0][0][0]

        return data


class FarmInfoSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    farm_name = fields.String(required=True)
    nucleos = fields.String(missing=None)
    crops = fields.List(fields.String(), missing=None)
    open_areas = fields.Float(missing=None)
    productive_areas = fields.Float(missing=None)
    vegetation_types = fields.List(fields.String(), missing=None)
    industries = fields.List(fields.String(), missing=None)
    aerodrome_lat = fields.Float(missing=None)
    aerodrome_lng = fields.Float(missing=None)


class FarmQuerySchema(Schema):
    owner_doc = fields.String(missing=None)

    @post_load
    def format(self, data: dict, **_):
        return {key: value for key, value in data.items() if value is not None}
