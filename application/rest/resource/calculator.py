from http import HTTPStatus
from flask import Blueprint, request, jsonify
from domain.service import CarbonCalculatorService
from ...schema import (
    CalculatorDataCollectSchema,
    CalculatorSettingsSchema,
    CalculatorQuerySchema
)
from ..security import Authorization, Role


def get_blueprint(
    auth: Authorization,
    service: CarbonCalculatorService
) -> Blueprint:
    bp = Blueprint('Calculator', __name__)
    data_collect_schema = CalculatorDataCollectSchema()
    config_schema = CalculatorSettingsSchema()
    calculator_query = CalculatorQuerySchema()

    @bp.get('/calculator')
    @auth.require_role(Role.READ_PROPERTIES)
    def get_all():
        user = auth.current_user
        query = calculator_query.load(request.args)

        if user and user.doc:
            query['owner_doc'] = user.doc

        calculator_bundles = service.get_all(query)
        return jsonify(calculator_bundles)

    @bp.get('/calculator/<string:_id>')
    @auth.require_role(Role.READ_PROPERTIES)
    def get_by_id(_id: str):
        carbon_data = service.get_by_id(_id)
        return jsonify(carbon_data)

    @bp.post('/calculator')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def calculate():
        data = data_collect_schema.load(request.json)
        bundle = service.calculate(data)
        return jsonify(bundle), HTTPStatus.CREATED

    @bp.delete('/calculator/<string:_id>')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def remove(_id: str):
        service.remove_by_id(_id)
        return jsonify({}), HTTPStatus.NO_CONTENT

    @bp.get('/calculator/settings')
    @auth.require_role(Role.READ_PROPERTIES)
    def get_config():
        return jsonify(service.load_settings())

    @bp.put('/calculator/settings')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def save_config():
        data = config_schema.load(request.json)
        return jsonify(service.save_settings(data))

    return bp
