from flask import Blueprint, jsonify, request, send_file
from pandas import DataFrame
from tempfile import NamedTemporaryFile
from datetime import datetime

from application.rest.security import Authorization, Role
from application.schema import FarmInfoSchema, FarmQuerySchema
from domain.service import FarmService
from .utils import geojson
from . import constants

MIME_XLSX = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


def get_blueprint(auth: Authorization, service: FarmService) -> Blueprint:
    bp = Blueprint('Farms', __name__)
    farm_schema = FarmInfoSchema()
    farm_query = FarmQuerySchema()

    def filter_by_owner() -> dict:
        query = farm_query.load(request.args)
        user = auth.current_user

        if user and user.doc:
            query['owner_doc'] = user.doc

        return query

    @bp.get('/farms')
    @auth.require_role(Role.READ_PROPERTIES)
    def summary_farms():
        query = filter_by_owner()
        summary = service.summary_farms(query)
        return jsonify(summary)

    @bp.get('/farms/<string:_id>')
    @auth.require_role(Role.READ_PROPERTIES)
    def farm_by_id(_id: str):
        farm = service.get_farm(_id)
        return jsonify(farm)

    @bp.put('/farms/<string:_id>')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def update_farm_info(_id: str):
        data = farm_schema.load(request.json)
        farm = service.update_farm_info(data, _id)
        return jsonify(farm)

    @bp.get('/farms/geojson')
    @auth.require_role(Role.READ_PROPERTIES)
    def farms_geojson():
        ids = request.args.get('ids')

        if ids is None:
            query = filter_by_owner()
            farms = service.search_farms(query)
        else:
            ids = [_id for _id in ids.split(',')]
            farms = service.get_farms(ids)

        return geojson.make_geojson_response(farms)

    @bp.post('/farms/geojson')
    @auth.require_role(Role.READ_PROPERTIES)
    def farms_large_geojson():
        data = request.get_json()
        ids = data['ids']

        if ids is None:
            query = filter_by_owner()
            farms = service.search_farms(query)
        else:
            ids = [_id for _id in ids.split(',')]
            farms = service.get_farms(ids)

        return geojson.make_geojson_response(farms)

    @bp.post('/farms/excel')
    @auth.require_role(Role.READ_PROPERTIES)
    def farms_excel():
        data = request.get_json()
        ids = data['ids']

        if ids is None:
            query = filter_by_owner()
            farms = service.search_farms(query)
        else:
            ids = [_id for _id in ids.split(',')]
            farms = service.get_farms(ids)

        df = DataFrame(data=farms)
        df = df.loc[:, df.columns != 'geometry']
        df['signature_date'] = df['signature_date'].apply(
            lambda x: x.strftime('%Y-%m-%d')
        )
        tmp_file = NamedTemporaryFile(prefix='farms_', suffix='.xlsx')
        df.to_excel(tmp_file.name, index=False)
        download_time = datetime.utcnow().strftime('%Y-%m-%d_%M-%S')

        return send_file(
            tmp_file,
            mimetype=MIME_XLSX,
            download_name=(f'propriedades__{download_time}.xlsx')
        )

    @bp.get('/farms/crops')
    @auth.require_role(Role.READ_PROPERTIES)
    def all_crops():
        return jsonify(constants.crops)

    return bp
