from flask import Flask
from flask_cors import CORS
from domain.service import (
    FarmService,
    PracticeService,
    CityService,
    SicarService,
    CarbonCalculatorService,
    StudyService,
    IcmbioService
)
from infrastructure import database
from infrastructure.repository import (
    FarmRepository,
    CityRepository,
    CalculatorRepository,
    PracticeRepository,
    StudyRepository,
    SicarRepository,
    SicarFarmRepository,
    IcmbioRepository,
    KafkaProducer
)
from .encoder import CustomJsonEncoder
from .error import error_bp
from .resource import (
    icmbio,
    owner,
    farms,
    cities,
    sicar,
    calculator,
    practices,
    studies
)
from .security import Authorization, Role


URL_PREFIX = '/api/v1/producer'


def create_server(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)
    app.json_encoder = CustomJsonEncoder
    app.url_map.strict_slashes = False
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(error_bp)
    db = database.get_database(app.config['MONGODB_SETTINGS'])

    CORS(app)
    is_auth_enabled = app.config['FLASK_ENV'] != 'development'
    auth = Authorization(app.config['INTROSPECTION_URI'], is_auth_enabled)
    auth.grant_role_for_any_request(Role.ADMIN)

    publisher = KafkaProducer({
        'bootstrap.servers': app.config['KAFKA_SERVER'],
        'client.id': 'PRODUCER',
        'message.max.bytes': 48 * 1024 ** 2
    })

    farm_repo = FarmRepository(db)
    farm_svc = FarmService(farm_repo, publisher)
    farm_bp = farms.get_blueprint(auth, farm_svc)
    app.register_blueprint(farm_bp, url_prefix=URL_PREFIX)

    owner_bp = owner.get_blueprint(auth, farm_svc)
    app.register_blueprint(owner_bp, url_prefix=URL_PREFIX)

    city_repo = CityRepository(db)
    city_svc = CityService(city_repo)
    city_bp = cities.get_blueprint(city_svc)
    app.register_blueprint(city_bp, url_prefix=URL_PREFIX)

    sicar_area_repo = SicarRepository(db)
    sicar_farm_repo = SicarFarmRepository(db)
    sicar_svc = SicarService(sicar_area_repo, sicar_farm_repo, city_repo)
    sicar_bp = sicar.get_blueprint(sicar_svc)
    app.register_blueprint(sicar_bp, url_prefix=URL_PREFIX)

    calculator_repo = CalculatorRepository(db)
    calculator_svc = CarbonCalculatorService(calculator_repo, farm_repo)
    calculator_svc.set_up_settings()
    calculator_bp = calculator.get_blueprint(auth, calculator_svc)
    app.register_blueprint(calculator_bp, url_prefix=URL_PREFIX)

    practice_repo = PracticeRepository(db)
    practice_svc = PracticeService(farm_repo, practice_repo)
    practice_bp = practices.get_blueprint(auth, practice_svc)
    app.register_blueprint(practice_bp, url_prefix=URL_PREFIX)

    studies_repo = StudyRepository(db)
    studies_svc = StudyService(studies_repo)
    studies_bp = studies.get_blueprint(studies_svc)
    app.register_blueprint(studies_bp, url_prefix=URL_PREFIX)

    icmbio_repo = IcmbioRepository(db)
    icmbio_svc = IcmbioService(icmbio_repo)
    icmbio_bp = icmbio.get_blueprint(icmbio_svc)
    app.register_blueprint(icmbio_bp, url_prefix=URL_PREFIX)

    return app
