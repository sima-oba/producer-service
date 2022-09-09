from application.schema import (
    CitySchema,
    FarmSchema,
    StudySchema,
    GeoParkSchema,
    EcoCorridorsSchema,
    GeoSitesSchema,
    IndigenousLandSchema,
    ConservationUnitSchema
)
from domain.service import (
    CityService,
    FarmService,
    StudyService,
    IcmbioService
)
from infrastructure import database
from infrastructure.repository import (
    CityRepository,
    FarmRepository,
    KafkaProducer,
    StudyRepository,
    IcmbioRepository
)
from .consumer import Consumer, ConsumerGroup


def start_consumer(config):
    db = database.get_database(config.MONGODB_SETTINGS)
    group = ConsumerGroup({
        'bootstrap.servers': config.KAFKA_SERVER,
        'group.id': 'PRODUCER',
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'
    })

    publisher = KafkaProducer({
        'bootstrap.servers': config.KAFKA_SERVER,
        'client.id': 'PRODUCER',
        'message.max.bytes': 48 * 1024 ** 2
    })

    farm_repo = FarmRepository(db)
    farm_svc = FarmService(farm_repo, publisher)
    farm_consumer = Consumer(FarmSchema(), farm_svc.add_farm)
    group.add(farm_consumer, 'FARM')

    city_repo = CityRepository(db)
    city_svc = CityService(city_repo)
    city_consumer = Consumer(CitySchema(), city_svc.save)
    group.add(city_consumer, 'CITY')

    study_repo = StudyRepository(db)
    study_svc = StudyService(study_repo)
    study_consumer = Consumer(StudySchema(), study_svc.save)
    group.add(study_consumer, 'STUDY')

    icmbio_repo = IcmbioRepository(db)
    icmbio_svc = IcmbioService(icmbio_repo)

    geopark_consumer = Consumer(
        GeoParkSchema(),
        icmbio_svc.save_geopark
    )
    consv_unit_consumer = Consumer(
        ConservationUnitSchema(),
        icmbio_svc.save_conservation_unit
    )
    ecocorridor_consumer = Consumer(
        EcoCorridorsSchema(),
        icmbio_svc.save_ecocorridor
    )
    geosite_consumer = Consumer(
        GeoSitesSchema(),
        icmbio_svc.save_geosite
    )
    indigenousland_consumer = Consumer(
        IndigenousLandSchema(),
        icmbio_svc.save_indigenousland
    )
    group.add(geopark_consumer, 'ICMBIO_GEOPARK')
    group.add(consv_unit_consumer, 'ICMBIO_CONSERVATION_UNIT')
    group.add(ecocorridor_consumer, 'ICMBIO_CORRIDOR')
    group.add(geosite_consumer, 'ICMBIO_SITE')
    group.add(indigenousland_consumer, 'ICMBIO_INDIGENOUS_LAND')

    group.wait()
