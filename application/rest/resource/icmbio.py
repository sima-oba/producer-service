from flask import Blueprint, request
from flask_cachecontrol import cache_for

from domain.service import IcmbioService
from .utils import geojson


def get_blueprint(service: IcmbioService) -> Blueprint:
    bp = Blueprint('ConservationUnits', __name__)

    @bp.get('/geosites/geojson')
    @cache_for(days=30)
    def search_geosite_geojson():
        return geojson.make_geojson_response(service.search_geosite(None))

    @bp.get('/geoparks/geojson')
    @cache_for(days=30)
    def search_park_geojson():
        return geojson.make_geojson_response(service.search_geopark(None))

    @bp.get('/ecocorridors/geojson')
    @cache_for(days=30)
    def search_ecocorridor_geojson():
        return geojson.make_geojson_response(service.search_ecocorridors(None))

    @bp.get('/indigenousland/geojson')
    @cache_for(days=30)
    def search_indigenousland_geojson():
        filter = request.args.to_dict()
        return geojson.make_geojson_response(service.search_indigenousland(filter))

    @bp.get('/conservation/geojson')
    @cache_for(days=30)
    def search_conservation_geojson():
        filter = request.args.to_dict()
        return geojson.make_geojson_response(service.search_consvunit(filter))

    @bp.get('/atlantic_forest/geojson')
    @cache_for(days=30)
    def search_atlantic_forest_geojson():
        return geojson.make_geojson_response(service.search_atlantic_forest())

    @bp.get('/biomes/geojson')
    @cache_for(days=30)
    def search_biomes_geojson():
        return geojson.make_geojson_response(service.search_biomes())

    @bp.get('/matopiba/geojson')
    @cache_for(days=30)
    def search_matopiba_geojson():
        return geojson.make_geojson_response(service.search_matopiba())

    @bp.get('/vegetation/geojson')
    @cache_for(days=30)
    def search_vegetation_geojson():
        return geojson.make_geojson_response(service.search_vegetation())

    return bp
