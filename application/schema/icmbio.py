from marshmallow import Schema, fields, validate, EXCLUDE, post_load

GEO_TYPES = ['Point', 'Polygon', 'MultiPolygon', 'Line', 'MultiLine']


class _GeometrySchema(Schema):
    type = fields.String(required=True, validate=validate.OneOf(GEO_TYPES))
    coordinates = fields.List(fields.Inferred())


class GeoParkSchema(Schema):
    imported_id = fields.String(required=True)
    type = fields.String(missing=None)
    name = fields.String(missing=None)
    latitude = fields.Float(missing=None)
    longitude = fields.Float(missing=None)
    state = fields.String(missing=None)
    description = fields.String(missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class EcoCorridorsSchema(Schema):
    imported_id = fields.String(required=True)
    name = fields.String(missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class GeoSitesSchema(Schema):
    imported_id = fields.String(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    name = fields.String(missing=None)
    state = fields.String(missing=None)
    type = fields.String(missing=None)
    description = fields.String(missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class IndigenousLandSchema(Schema):
    imported_id = fields.String(required=True)
    location = fields.String(missing=None)
    population = fields.Integer(missing=None)
    groups = fields.String(missing=None)
    state = fields.String(missing=None)
    city = fields.String(missing=None)
    stage = fields.String(missing=None)
    status = fields.String(missing=None)
    title = fields.String(missing=None)
    document = fields.String(missing=None)
    date = fields.DateTime(format='%Y-%m-%d', missing=None)
    extension = fields.String(missing=None)
    area_name = fields.String(missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class ConservationUnitSchema(Schema):
    imported_id = fields.String(required=True)
    name = fields.String(missing=None)
    category = fields.String(missing=None)
    group = fields.String(missing=None)
    sphere = fields.String(missing=None)
    creation_year = fields.String(missing=None)
    quality = fields.String(missing=None)
    legal_act = fields.String(missing=None)
    last_update = fields.DateTime(format='%d/%m/%Y', missing=None)
    original_name = fields.String(missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class AtlanticForestSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    imported_id = fields.String(data_key='imported_id_0', required=True)
    geometry = fields.Nested(_GeometrySchema, required=True)


class BiomeSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    imported_id = fields.String(data_key='ID_0', required=True)
    name = fields.String(required=True)
    geometry = fields.Nested(_GeometrySchema, required=True)


class MatopibaSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    state = fields.String(data_key='estado', required=True)
    geometry = fields.Nested(_GeometrySchema, required=True)

    @post_load
    def transform(self, data: dict, **_):
        data['imported_id'] = data['state']
        return data


class VegetationSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    imported_id = fields.String(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    description = fields.String(required=True)
    source = fields.String(required=True)
    geometry = fields.Nested(_GeometrySchema, required=True)
