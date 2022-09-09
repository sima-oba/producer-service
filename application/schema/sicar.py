from marshmallow import Schema, fields, validate, post_load, EXCLUDE

GEO_TYPES = ['Point', 'Polygon', 'MultiPolygon', 'Line', 'MultiLine']


class _GeometrySchema(Schema):
    type = fields.String(required=True, validate=validate.OneOf(GEO_TYPES))
    coordinates = fields.List(fields.Inferred())


class SicarAreaSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    idf = fields.Integer(data_key='IDF', required=True)
    subject = fields.String(required=True)
    description = fields.String(data_key='NOM_TEMA', required=True)
    area_number = fields.Float(data_key='NUM_AREA', required=True)
    geometry = fields.Nested(_GeometrySchema, required=True)


class SicarFarmSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    farm_code = fields.String(data_key='COD_IMOVEL', required=True)
    state = fields.String(data_key='COD_ESTADO', required=True)
    city = fields.String(data_key='NOM_MUNICI', required=True)
    property_type = fields.String(data_key='TIPO_IMOVE', required=True)
    status = fields.String(data_key='SITUACAO', missing=None)
    condition = fields.String(data_key='CONDICAO_I', missing=None)
    geometry = fields.Nested(_GeometrySchema, required=True)


class SicarQuery(Schema):
    subject = fields.String(missing=None)
    city_geoid = fields.String(missing=None)

    @post_load
    def transform(self, data: dict, **_):
        return {k: v for k, v in data.items() if v is not None}
