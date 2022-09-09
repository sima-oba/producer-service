from flask import Blueprint, jsonify
from flask_cachecontrol import cache_for

from domain.service import CityService
from .utils import geojson


def get_blueprint(service: CityService) -> Blueprint:
    bp = Blueprint('Cities', __name__)

    @bp.get('/cities')
    def all_cities():
        return jsonify(service.summary())

    @bp.get('/cities/geojson')
    @cache_for(weeks=1)
    def all_cities_geojson():
        cities = service.get_all()
        return geojson.make_geojson_response(cities)

    return bp
