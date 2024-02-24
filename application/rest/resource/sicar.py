
import geopandas
import logging
import patoolib
from flask import Blueprint, request, jsonify
from flask_cachecontrol import cache_for
from fiona.errors import DriverError
from marshmallow import Schema, ValidationError
from shapely.geometry import mapping
from typing import List

from application.schema import SicarAreaSchema, SicarFarmSchema, SicarQuery
from domain.service import SicarService
from .utils import geojson, sys

MIMETYPES = (
    'application/zip',
    'application/x-zip-compressed',
    'multipart/x-zip'
)

AREAS_OF_INTEREST = (
    'APP',
    'AREA_CONSOLIDADA',
    'RESERVA_LEGAL',
    'VEGETACAO_NATIVA'
)

log = logging.getLogger(__name__)


def _extract_zip(zip_file: str, out_dir: str):
    patoolib.extract_archive(archive=zip_file, outdir=out_dir)


def _extract_shp(zip_file: str, schema: Schema, subject: str) -> List[dict]:
    df = geopandas.read_file(zip_file, encoding='utf-8')
    contents = []

    for row in df.iterrows():
        data = row[1].to_dict()
        data['subject'] = subject
        data['geometry'] = mapping(data['geometry'])

        try:
            data = schema.load(data)
            contents.append(data)
        except ValidationError as e:
            data.pop('geometry')
            log.warning(
                f'Error validating {schema.__class__.__name__} | '
                f'errors: {e} | '
                f'contents (geometry omitted): {data}'
            )

    return contents


def get_blueprint(service: SicarService) -> Blueprint:
    bp = Blueprint('Sicar', __name__)
    area_schema = SicarAreaSchema()
    farm_schema = SicarFarmSchema()
    sicar_query = SicarQuery()

    @bp.get('/sicar/areas')
    @cache_for(hours=2)
    def get_areas_geojson():
        query = sicar_query.load(request.args)
        sicar = service.search_areas(query)
        return geojson.make_geojson_response(sicar)

    @bp.get('/sicar/areas2')
    @cache_for(hours=2)
    def get_areas2_geojson():
        query = sicar_query.load(request.args)

        for k, v in query.items():
            query[k] = {'$in': ','.split(v)}

        sicar = service.search_areas(query)
        return geojson.make_geojson_response(sicar)

    @bp.get('/sicar/farms')
    @cache_for(hours=2)
    def get_farms_geojson():
        city_geoid = request.args.get('city_geoid')

        if city_geoid is None:
            ValidationError({'city_geoid': 'Missing required field'})

        farms = service.search_farms(city_geoid)
        return geojson.make_geojson_response(farms)

    @bp.post('/cities/<string:city_id>/sicar')
    def import_sicar(city_id: str):
        tmp_dir = sys.make_tmp_dir('sicar')
        tmp_zip = tmp_dir + '/sicar.zip'
        file = sys.get_file('sicar', *MIMETYPES)
        file.save(tmp_zip)

        imported_items = 0
        _extract_zip(tmp_zip, tmp_dir)

        for subject in AREAS_OF_INTEREST:
            try:
                path = f'{tmp_dir}/{subject}.zip'
                data = _extract_shp(path, area_schema, subject)
                service.save_areas(data, city_id)
                imported_items += len(data)
            except DriverError as e:
                log.warn(f'Unable to extract {path}. Reason: {e}')
                raise ValidationError({'sicar': 'Invalid file content'})

        try:
            path = f'{tmp_dir}/AREA_IMOVEL.zip'
            data = _extract_shp(path, farm_schema, 'AREA_IMOVEL')
            service.save_farms(data, city_id)
        except DriverError as e:
            log.warn(f'Unable to extract {path}. Reason: {e}')
            raise ValidationError({'sicar': 'Invalid file content'})

        sys.rm_dir(tmp_dir)
        return jsonify({'imported_items': imported_items})

    return bp
