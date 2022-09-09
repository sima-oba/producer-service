from flask import Blueprint, request, jsonify

from domain.service import StudyService
from ...schema import StudyQuery
from . import utils


def get_blueprint(service: StudyService) -> Blueprint:
    bp = Blueprint('Studies', __name__)
    query = StudyQuery()

    def _search():
        filter = query.load(request.args)
        return service.search_studies(filter)

    @bp.get('/studies')
    def search():
        return jsonify(_search())

    @bp.get('/studies/geojson')
    def search_geojson():
        studies = _search()
        return utils.make_geojson_response(studies)

    @bp.get('/studies/<string:_id>')
    def get_study(_id: str):
        return jsonify(service.get_study(_id))

    @bp.get('/studies/<string:_id>/geojson')
    def get_study_geojson(_id: str):
        study = service.get_study(_id)
        return utils.make_geojson_response([study])

    return bp
