from flask import Flask
import json
from os.path import abspath, dirname
import pytest
from domain.service import (
    CityService,
    FarmService,
    SicarService,
    StudyService,
    CarbonCalculatorService
)
from handlers.route_handlers import (
    configure_routes_calculator,
    configure_routes_cities,
    configure_routes_farms,
    configure_routes_owner,
    configure_routes_sicar,
)
from infrastructure.database import get_database
from . import TestConfig as config
from infrastructure.repository import (
    CalculatorRepository,
    CityRepository,
    FarmRepository,
    KafkaProducer,
    StudyRepository
)


db = get_database(config.MONGODB_SETTINGS)
publisher = KafkaProducer({
    'bootstrap.servers': config.KAFKA_SERVER,
    'client.id': 'PRODUCER',
    'message.max.bytes': 33554432
})
farm_repo = FarmRepository(db)
farm_service = FarmService(farm_repo, publisher)
city_repo = CityRepository(db)
city_Service = CityService(city_repo)
sicar_service = SicarService(city_repo, publisher)
calculator_repo = CalculatorRepository(db)
calculator_service = CarbonCalculatorService(calculator_repo, farm_repo)
studies_repo = StudyRepository(db)
studies_svc = StudyService(studies_repo)
calculator_service.set_up_settings()


def mock_kafka():
    from application import kafka
    kafkaresult = kafka.start_consumer(config)
    return kafkaresult


def build_test_requeriments(client):
    url = '/owners'

    mjson = {
        "defaulting": False,
        "name": "Marcos Dantas da Silva",
        "doc": "55692199000155"
    }

    client.post(url, json=mjson)
    url = '/farms'

    mjson = {
        "farm_code": "BA-2902500-5B08A644E20E41B18E44E1E6AB082109",
        "farm_name": "Fazenda Santa Helena",
        "state": "BA",
        "city": "Baianópolis",
        "property_type": "IRU",
        "signature_date": "2001-05-15",
        "owner_doc": "55692199000155",
        "area": 483.3797,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        567362.229999999864958,
                        8631191.339999999850988
                    ],
                    [
                        567544.48000000056345,
                        8631049.189999999478459
                    ],
                    [
                        567611.370000000693835,
                        8630969.259999999776483
                    ],
                    [
                        567624.260000000940636,
                        8630953.5
                    ]
                ]
            ]
        }
    }

    city_data = {
        "geoid": "1600303",
        "name": "Macapá",
        "state": "Amapá",
        "microrregiao": {
            "id": 16003,
            "nome": "Macapá",
            "mesorregiao": {
                "id": 1602,
                "nome": "Sul do Amapá",
                "UF": {
                    "id": 16,
                    "sigla": "AP",
                    "nome": "Amapá",
                    "regiao": {
                        "id": 1,
                        "sigla": "N",
                        "nome": "Norte"
                    }
                }
            }
        },
        "regiao-imediata": {
            "id": 160001,
            "nome": "Macapá",
            "regiao-intermediaria": {
                "id": 1601,
                "nome": "Macapá",
                "UF": {
                    "id": 16,
                    "sigla": "AP",
                    "nome": "Amapá",
                    "regiao": {
                        "id": 1,
                        "sigla": "N",
                        "nome": "Norte"
                    }
                }
            }
        }
    }

    city_Service.save(city_data)
    client.post(url, json=mjson)


@pytest.fixture
def producer_prop(clientinstance):
    url = '/farms/geojson'
    response = clientinstance.get(url)
    response = response.get_data().decode("utf-8")
    _id = json.loads((response))['features'][0]['properties']['_id']
    return _id


@pytest.fixture
def clientinstance():
    app = Flask(__name__)
    configure_routes_farms(app, farm_service)
    configure_routes_owner(app, farm_service)
    configure_routes_cities(app, city_Service)
    configure_routes_sicar(app, sicar_service)
    configure_routes_calculator(app, calculator_service)
    client = app.test_client()
    build_test_requeriments(client)
    return client


def test_kafka_consumer(mocker):
    mocker.patch('application.kafka.start_consumer', return_value=1)
    assert mock_kafka() == 1


def test_farm_summary(clientinstance):
    url = '/farms?filter={ input: [], as: "test", cond:}'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_farm_by_id(clientinstance, producer_prop):
    url = f'/farms/{producer_prop}'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_farm_put(clientinstance, producer_prop):
    url = f'/farms/{producer_prop}'

    mjson = {
        "farm_code": "BA-2902500-5B08A644E20E41B18E44E1E6AB082109",
        "farm_name": "Fazenda Santa Helena",
        "state": "BA",
        "city": "Baianópolis",
        "property_type": "IRU",
        "signature_date": "2001-05-15",
        "owner_doc": "55692199000155",
        "area": 483.3797,
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        567362.229999999864958,
                        8631191.339999999850988
                    ],
                    [
                        567544.48000000056345,
                        8631049.189999999478459
                    ],
                    [
                        567611.370000000693835,
                        8630969.259999999776483
                    ],
                    [
                        567624.260000000940636,
                        8630953.5
                    ]
                ]
            ]
        }
    }

    posting = clientinstance.put(url, json=mjson)
    assert posting.status_code == 200


def _test_farm_geojson(clientinstance):
    url = '/farms/geojson'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_farm_crops(clientinstance):
    url = '/farms/crops'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_owner_route(clientinstance):
    url = '/owners/df2381fc-876e-4ac5-b970-59d74b635239'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_cities_get(clientinstance):
    url = '/cities'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_sicar_post(clientinstance):
    url = '/cities'
    response = clientinstance.get(url)
    response = response.get_data().decode("utf-8")
    _id = json.loads((response).replace('[', '').replace(']', ''))['_id']
    url = f'/cities/{_id}/sicar'

    data = {}
    data['sicar'] = (f'{dirname(abspath(__name__))}/test/SHAPE_2907905.zip', 'sicar.zip')  # noqa
    posting = clientinstance.post(url, data=data, content_type='multipart/form-data')  # noqa
    assert posting.status_code == 200


def test_calculator_get(clientinstance):
    url = '/calculator'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_calculator_get_by_id(clientinstance):
    url = '/calculator'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def _test_calculator_post(clientinstance, producer_prop):
    url = '/calculator'
    mjson = {
        'farm_id': producer_prop,
        'synthetic_n_fertilizer_teor_type3': 1,
        'green_adubation': 1,
        'synthetic_n_fertilizer_teor_type3_second_crop': 1,
        'organization': '',
        'others_type1_kg_second_crop': 1,
        'diesel_b10_stationary_operation': 1,
        'average_productivity_second_crop': 1,
        'synthetic_n_fertilizer_type2_kg': 1,
        'resp_name': '',
        'others_type1_kg': 1,
        'agricultural_plaster': 1,
        'agricultural_plaster_second_crop': 1,
        'synthetic_n_fertilizer_teor_type1': 1,
        'organic_n_fertilizer_type1_kg_second_crop': 1,
        'biome_2': 1,
        'area_organic_soils': 1,
        'biome_3': 1,
        'gasoline_mechanical_operation': 1,
        'waste_field': 1,
        'synthetic_n_fertilizer_type1_kg': 1,
        'biome_1': 1,
        'biome_3_coverage': 1,
        'cultivated_area': 1,
        'grassy_type1_kg': 1,
        'diesel_b10_mechanical_operation': 1,
        'cultivation_system': {
            'average_productivity': 1,
            'average_productivity_second_crop': 1,
            'cultivation_system': 1
        },
        'average_productivity': 1,
        'synthetic_n_fertilizer_teor_type2': 1,
        'synthetic_n_fertilizer_teor_type1_second_crop': 1,
        'organic_n_fertilizer_type1_kg': 1,
        'calcitic_limestone': 1,
        'synthetic_n_fertilizer_type2_kg_second_crop': 1,
        'cultivated_area_second_crop': 1,
        'decomposition': {
            'waste_field_second_crop': 1,
            'waste_field': 1
        },
        'stock': {
            'rl': 1,
            'app': 1,
            'forest_surplus': 1
        },
        'fuel_consumption': {
            'gasoline_mechanical_operation': 1,
            'diesel_b10_mechanical_operation': 1,
            'gasoline_stationary_operation': 1,
            'diesel_b10_stationary_operation': 1,
            'hydrous_ethanol_mechanical_operation': 1,
            'hydrous_ethanol_stationary_operation': 1,
            'transport_production_diesel_b10': 1
        },
        'farm_info': {
            'cultivated_area': 1,
            'coverage_use': 1,
            'cultivated_area_second_crop': 1,
            'biome_1': 1,
            'biome_1_coverage': 1,
            'biome_2': 1,
            'biome_2_coverage': 1,
            'biome_3': 1,
            'biome_3_coverage': 1
        },
        'correction': {
            'calcitic_limestone': 1,
            'calcitic_limestone_second_crop': 1,
            'dolomitic_limestone': 1,
            'dolomitic_limestone_second_crop': 1,
            'agricultural_plaster': 1,
            'agricultural_plaster_second_crop': 1
        },
        'soil_characteristics': {
            'area_organic_soils': 1
        },
        'general_info': {
            'farm_id': producer_prop,
            'resp_name': '',
            'organization': '',
            'date': '2014-12-22T03:12:58.019077+00:00'
        },
        'nitrogen_fertilization': {
            'synthetic_n_fertilizer_type1_kg': 1,
            'synthetic_n_fertilizer_type2_kg': 1,
            'synthetic_n_fertilizer_type3_kg': 1,
            'synthetic_n_fertilizer_type1_kg_second_crop': 1,
            'synthetic_n_fertilizer_type2_kg_second_crop': 1,
            'synthetic_n_fertilizer_type3_kg_second_crop': 1,
            'synthetic_n_fertilizer_teor_type1': 1,
            'synthetic_n_fertilizer_teor_type2': 1,
            'synthetic_n_fertilizer_teor_type3': 1,
            'synthetic_n_fertilizer_teor_type1_second_crop': 1,
            'synthetic_n_fertilizer_teor_type2_second_crop': 1,
            'synthetic_n_fertilizer_teor_type3_second_crop': 1,
            'urea_type1': 1,
            'urea_type1_second_crop': 1,
            'organic_n_fertilizer_type1_kg': 1,
            'organic_n_fertilizer_type1_kg_second_crop': 1,
            'green_adubation': 1,
            'green_adubation_second_crop': 1,
            'grassy_type1_kg': 1,
            'grassy_type1_kg_second_crop': 1,
            'others_type1_kg': 1,
            'others_type1_kg_second_crop': 1
        },
        'grassy_type1_kg_second_crop': 1,
        'transport_production_diesel_b10': 1,
        'date': '2014-12-22T03:12:58.019077+00:00',
        'urea_type1': 1,
        'synthetic_n_fertilizer_type1_kg_second_crop': 1,
        'urea_type1_second_crop': 1,
        'dolomitic_limestone': 1,
        'calcitic_limestone_second_crop': 1,
        'synthetic_n_fertilizer_teor_type2_second_crop': 1,
        'waste_field_second_crop': 1,
        'hydrous_ethanol_mechanical_operation': 1,
        'hydrous_ethanol_stationary_operation': 1,
        'coverage_use': 1,
        'gasoline_stationary_operation': 1,
        'synthetic_n_fertilizer_type3_kg_second_crop': 1,
        'energy_consumption': 1,
        'dolomitic_limestone_second_crop': 1,
        'biome_1_coverage': 1,
        'biome_2_coverage': 1,
        'synthetic_n_fertilizer_type3_kg': 1,
        'green_adubation_second_crop': 1,
    }

    posting = clientinstance.post(url, json=mjson)
    assert posting.status_code == 201


def test_calculator_config(clientinstance):
    url = '/calculator/config'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 200


def test_calculator_config_put(clientinstance):
    url = '/calculator/config'

    mjson = {
        'land_occupation_10': 1,
        'land_occupation_4': 1,
        'organic_soils_cultivation': 1,
        'land_occupation_14': 1,
        'consumption_ethanol_co2_stationary_source': 1,
        'urea_co2': 1,
        'corn_nbg_second_crop': 1,
        'urea_n2o': 1,
        'preserved_native_forest_soil_23': 1,
        'preserved_native_forest_soil_17': 1,
        'preserved_native_forest_soil_3': 1,
        'preserved_native_forest_soil_31': 1,
        'methane': 1,
        'preserved_native_forest_soil_19': 1,
        'preserved_native_forest_soil_20': 1,
        'green_fertilizer_3': 1,
        'purchase_of_electricity_2019': 1,
        'land_occupation_9': 1,
        'preserved_native_forest_soil_8': 1,
        'land_occupation_1': 1,
        'soy_slope': 1,
        'diesel_n20_stationary_source': 1,
        'preserved_native_forest_soil_13': 1,
        'consumption_gasoline': 1,
        'volatilization_n_residue': 1,
        'corn_intercept_second_crop': 1,
        'diesel_c02_stationary_source': 1,
        'preserved_native_forest_soil_12': 1,
        'nitrogen_fertilization_green_fertilizer': 1,
        'corn_nag_second_crop': 1,
        'organic_n_fertilizer': 1,
        'corn_frac_dm_second_crop': 1,
        'land_occupation_12': 1,
        'soy_nag': 1,
        'preserved_native_forest_soil_21': 1,
        'no_tillage_system': 1,
        'leaching': 1,
        'preserved_native_forest_soil_24': 1,
        'preserved_native_forest_soil_15': 1,
        'diesel_n2o_mobile_source': 1,
        'consumption_biodiesel_n20_mobile_source': 1,
        'no_tillage_system_coverage': 1,
        'synthetic_fertilization': 1,
        'nitrous_oxide': 1,
        'diesel_b10': 1,
        'preserved_native_forest_soil_2': 1,
        'preserved_native_forest_soil_6': 1,
        'atmospheric_deposition': 1,
        'leaching_n_fertilizer': 1,
        'nitrogen_loss': 1,
        'preserved_native_forest_soil_9': 1,
        'land_occupation_11': 1,
        'preserved_native_forest_soil_10': 1,
        'preserved_native_forest_soil_4': 1,
        'diesel_ch4_mobile_source': 1,
        'regular_gasoline': 1,
        'preserved_native_forest_soil_18': 1,
        'land_occupation_8': 1,
        'soy_nbg': 1,
        'preserved_native_forest_soil_28': 1,
        'green_fertilizer_2': 1,
        'diesel_c02_mobile_source': 1,
        'corn_rbg_bio_second_crop': 1,
        'soy_intercept': 1,
        'preserved_native_forest_soil_29': 1,
        'land_occupation_5': 1,
        'synthetic_n_volatilization': 1,
        'purchase_of_electricity_2020': 1,
        'soy_rbg_bio': 1,
        'diesel_ch4_stationary_source': 1,
        'preserved_native_forest_soil_27': 1,
        'calcitic_limestone': 1,
        'preserved_native_forest_soil_26': 1,
        'land_occupation_2': 1,
        'land_occupation_3': 1,
        'consumption_ethanol_n20_stationary_source': 1,
        'agricultural_plaster': 1,
        'dolomitic_limestone': 1,
        'urea_n_volatilization': 1,
        'preserved_native_forest_soil_30': 1,
        'consumption_ethanol_ch4_stationary_source': 1,
        'preserved_native_forest_soil_1': 1,
        'land_occupation_15': 1,
        'land_occupation_7': 1,
        'preserved_native_forest_soil_22': 1,
        'soy_frac_dm': 1,
        'land_occupation_16': 1,
        'preserved_native_forest_soil_5': 1,
        'land_occupation_6': 1,
        'corn_slope_second_crop': 1,
        'preserved_native_forest_soil_7': 1,
        'green_fertilizer_1': 1,
        'consumption_biodiesel_co2_mobile_source': 1,
        'land_occupation_13': 1,
        'land_occupation_17': 1,
        'consumption_biodiesel_ch4_mobile_source': 1,
        'preserved_native_forest_soil_16': 1,
        'conventional_planting_system': 1,
        'preserved_native_forest_soil_11': 1,
        'preserved_native_forest_soil_25': 1,
        'preserved_native_forest_soil_14': 1
    }

    posting = clientinstance.put(url, json=mjson)
    assert posting.status_code == 200


def test_studies_route(clientinstance):
    url = '/studies?filter={ input: [], as: "test", cond:}'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 404


def test_studies_geojson(clientinstance):
    url = '/studies/geojson?filter={ input: [], as: "test", cond:}'

    response = clientinstance.get(url)
    assert response.get_data() != b''
    assert response.status_code == 404
