from flask import Blueprint, jsonify, request
from http import HTTPStatus
from marshmallow import Schema
from marshmallow.exceptions import ValidationError
from typing import Dict

from application.rest.security import Authorization, Role
from domain.model import PracticeType
from domain.service import PracticeService
from application.schema.practices import (
    ControlledTrafficSystemSchema,
    CorrectiveQualitySchema,
    CropRotationSchema,
    IrrigationUseEfficiencySchema,
    PhytosanitarySchema,
    SoilRechargeAndMoistureSchema,
    SoilTemperatureSchema,
    SustainableSchema,
    WaterRunoffContainmentSchema,
    PracticeQuery,
    ReportQuery
)

_schemas: Dict[PracticeType, Schema] = {
    PracticeType.CONTROLLED_TRAFFIC_SYSTEM: ControlledTrafficSystemSchema(),
    PracticeType.CORRECTIVE_QUALITY: CorrectiveQualitySchema(),
    PracticeType.CROP_ROTATION: CropRotationSchema(),
    PracticeType.IRRIGATION_USE_EFFICIENCY: IrrigationUseEfficiencySchema(),
    PracticeType.PHYTOSANITARY: PhytosanitarySchema(),
    PracticeType.SOIL_RECHARGE_AND_MOISTURE: SoilRechargeAndMoistureSchema(),
    PracticeType.SOIL_TEMPERATURE: SoilTemperatureSchema(),
    PracticeType.SUSTAINABLE: SustainableSchema(),
    PracticeType.WATER_RUNOFF_CONTAINMENT: WaterRunoffContainmentSchema()
}


def _parse_practice_type() -> PracticeType:
    data = request.json

    if not isinstance(data, dict):
        raise ValidationError('Missing request body')

    if data.get('practice_type') is None:
        raise ValidationError({'practice_type': 'Missing data'})

    try:
        return PracticeType[data['practice_type']]
    except KeyError:
        raise ValidationError({'practice_type': 'Unexpected practice type'})


def get_blueprint(auth: Authorization, service: PracticeService) -> Blueprint:  # noqa: C901
    bp = Blueprint('Practices', __name__)
    practice_query = PracticeQuery()
    report_query = ReportQuery()

    @bp.get('/practices')
    @auth.require_role(Role.READ_PROPERTIES)
    def get_practices():
        filter = practice_query.load(request.args)
        user = auth.current_user

        if user and user.doc:
            filter['owner_doc'] = user.doc

        return jsonify(service.find_all(filter))

    @bp.get('/practices/<string:_id>')
    @auth.require_role(Role.READ_PROPERTIES)
    def get_practice_by_id(_id: str):
        return jsonify(service.find_by_id(_id))

    @bp.post('/practices')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def add_practice():
        practice_type = _parse_practice_type()
        data = _schemas[practice_type].load(request.json)

        if data.get('evaluation'):
            auth.verify_permission(Role.MANAGE_PROPERTIES)

        practice = service.add(data)
        return jsonify(practice), HTTPStatus.CREATED

    @bp.put('/practices/<string:_id>')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def evaluate_practice(_id: str):
        practice_type = _parse_practice_type()
        data = _schemas[practice_type].load(request.json)

        if data.get('evaluation') is None:
            raise ValidationError({'evaluation': 'Missing required field'})

        practice = service.update(data, _id)
        return jsonify(practice)

    @bp.delete('/practices/<string:_id>')
    @auth.require_role(Role.WRITE_PROPERTIES)
    def remove_practice(_id: str):
        service.remove(_id)
        return jsonify(None), HTTPStatus.NO_CONTENT

    @bp.get('/practices/report')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def get_practice_report():
        query = report_query.load(request.args)

        if query.get('practice_type') is None:
            raise ValidationError({'practice_type': 'Missing param'})

        totals = service.get_practice_report(query)
        return jsonify(totals)

    @bp.get('/practices/report/total')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def get_practice_totals():
        query = report_query.load(request.args)
        totals = service.get_practice_totals(query)
        return jsonify(totals)

    return bp
