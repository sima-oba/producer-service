from http import HTTPStatus
from flask import request, jsonify
from application.schema import (
    FarmInfoSchema,
    CalculatorSettingsSchema,
    CalculatorDataCollectSchema,
    CalculatorQuerySchema,
    OwnerSchema,
    FarmSchema,
    StudyQuery
)
from domain.service import (
    CarbonCalculatorService,
    SicarService,
    CityService,
    FarmService,
    StudyService
)
from application.rest.resource import (
    constants,
    utils,
)


def configure_routes_farms(app, service: FarmService):
    farm_schema = FarmInfoSchema()
    schema = FarmSchema()

    @app.route('/farms')
    def summary_farms():
        _filter = request.args.to_dict()
        summary = [
            {
                '_id': farm._id,
                'farm_name': farm.farm_name
            }
            for farm in service.search_farms(_filter)
        ]
        return jsonify(summary)

    @app.route('/farms/<string:_id>')
    def farm_by_id(_id: str):
        return jsonify(service.get_farm(_id))

    @app.route('/farms/<string:_id>', methods=['PUT'])
    def update_farm_info(_id: str):
        data = farm_schema.load(request.json)
        farm = service.update_farm_info(data, _id)
        return jsonify(farm)

    @app.route('/farms/geojson')
    def farms_geojson():
        ids = request.args.get('ids')

        if ids is None:
            results = service.search_farms()
        else:
            results = [service.get_farm(_id) for _id in ids.split(',')]

        results = utils.export_feature_collection(results, 'geometry')
        return jsonify(results)

    @app.route('/farms/crops')
    def all_crops():
        return jsonify(constants.crops)

    @app.route('/farms', methods=['POST'])
    def add_farm():
        data = schema.load(request.json)
        _owner = service.add_farm(data)
        return jsonify(_owner)


def configure_routes_owner(app, service: FarmService):

    owner_schema = OwnerSchema()

    @app.route('/owners/<string:_id>')
    def owner_by_id(_id: str):
        return jsonify(service.get_owner_by_id(_id))

    @app.route('/owners', methods=['POST'])
    def add_owner():
        data = owner_schema.load(request.json)
        _owner = service.add_owner(data)
        return jsonify(_owner)


def configure_routes_cities(app, service: CityService):

    @app.route('/cities')
    def all_cities():
        return jsonify(service.get_all())


def configure_routes_sicar(app, service: SicarService):

    # MIMETYPES = (
    #     'application/zip',
    #     'application/x-zip-compressed',
    #     'multipart/x-zip'
    # )

    @app.route('/cities/<string:_id>/sicar', methods=['POST'])
    def add_sicar(_id: str):
        # file = utils.get_file('sicar', *MIMETYPES)
        # data = file.read()
        # city = service.send_sicar(data, _id)
        # return jsonify(city)
        return jsonify({})


def configure_routes_calculator(app, service: CarbonCalculatorService):

    data_collect_schema = CalculatorDataCollectSchema()
    config_schema = CalculatorSettingsSchema()
    producer_schema = CalculatorQuerySchema()

    @app.route('/calculator')
    def calculator_all():
        data = request.args.get('producer_id')

        if data is not None:
            _id = producer_schema.load(data)
            return jsonify(service.get_by_producer(_id))

        return jsonify(service.get_all())

    @app.route('/calculator/<string:_id>')
    def calculator_by_id(_id: str):
        carbon_data = service.get_by_id(_id)
        return jsonify(carbon_data)

    @app.route('/calculator', methods=['POST'])
    def add_calculator():
        data = data_collect_schema.load(request.json)
        bundle = service.calculate(data)
        return jsonify(bundle), HTTPStatus.CREATED

    @app.route('/calculator/config')
    def get_config():
        return jsonify(service.load_settings())

    @app.route('/calculator/config', methods=['PUT'])
    def save_config():
        data = config_schema.load(request.json)
        return jsonify(service.save_settings(data))


def configure_routes_studies(app, service: StudyService):

    query = StudyQuery()

    def _search():
        filter = query.load(request.args)
        return service.search_studies(filter)

    @app.route('/studies')
    def search():
        return jsonify(_search())

    @app.route('/studies/geojson')
    def search_geojson():
        studies = _search()
        features = utils.export_feature_collection(studies)
        return jsonify(features)

    @app.route('/studies/<string:_id>')
    def get_study(_id: str):
        return jsonify(service.get_study(_id))

    @app.route('/studies/<string:_id>/geojson')
    def get_study_geojson(_id: str):
        study = service.get_study(_id)
        features = utils.export_feature_collection([study])
        return jsonify(features)
