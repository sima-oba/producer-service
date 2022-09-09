from flask import Blueprint, jsonify, request

from application.rest.security import Authorization, Role
from application.schema import FarmInfoSchema, FarmQuerySchema
from domain.service import FarmService
from .utils import geojson
from . import constants


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

    @bp.get('/farms/crops')
    @auth.require_role(Role.READ_PROPERTIES)
    def all_crops():
        return jsonify(constants.crops)

    return bp
