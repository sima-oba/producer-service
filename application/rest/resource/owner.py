import glob
import geopandas as gpd
import logging
import os
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from shapely import geometry
from zipfile import ZipFile

from application.schema import OwnerSchema, FarmSchema
from application.rest.security import Authorization, Role
from domain.service import FarmService
from .utils import sys

MIMETYPES = (
    'application/zip',
    'application/x-zip-compressed',
    'multipart/x-zip'
)

log = logging.getLogger(__name__)


def _extract_owner(data: dict) -> str:
    if data['Telefone1']:
        data['Telefone1'].replace(' ', '')

    payload = {
        'doc':          data['CNPJ___CPF'],
        'name':         data['Nome_Parce'].title(),
        'email':        data['Email'],
        'phone':        data['Telefone1'],
        'defaulting':   data.get('Inadimplente', False)
    }

    return payload


def _extract_farm(data: dict) -> str:
    coordinates = geometry.mapping(data['geometry'])['coordinates']
    coordinates = [[coord[:2] for coord in coordinates[0]]]
    payload = {
        'farm_code':        data['COD_IMOVEL'],
        'farm_name':        data['nome_area'],
        'state':            data['COD_ESTADO'],
        'city':             data['NOM_MUNICI'],
        'property_type':    data['TIPO_IMOVE'],
        'area':             data['area_hecta'],
        'signature_date':   data['Data_de_As'],
        'owner_doc':        data['CNPJ___CPF'],
        'geometry': {
            'type': 'Polygon',
            'coordinates': coordinates
        }
    }

    return payload


def _extract_dataframe(shape) -> gpd.GeoDataFrame:  # nosec
    if not os.path.exists('/tmp/owners'):
        os.mkdir('/tmp/owners')

    shape.save('/tmp/owners/owners.zip')

    with ZipFile('/tmp/owners/owners.zip', 'r') as zip:
        zip.extractall('/tmp/owners')
        shp_path = glob.glob('/tmp/owners/*.shp')[0]
        df = gpd.read_file(shp_path)
        
        return df.to_crs('epsg:4326')


def get_blueprint(auth: Authorization, service: FarmService) -> Blueprint:
    bp = Blueprint('Owners', __name__)
    owner_schema = OwnerSchema()
    farm_schema = FarmSchema()

    @bp.get('/owners')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def get_all():
        return jsonify(service.get_owners())

    @bp.get('/owners/<string:_id>')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def by_id(_id: str):
        return jsonify(service.get_owner_by_id(_id))

    @bp.get('/owners/import')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def get_import_info():
        import_info = service.get_imported_info()
        return jsonify(import_info)

    @bp.post('/owners/import')
    @auth.require_role(Role.MANAGE_PROPERTIES)
    def import_owners():
        file = sys.get_file('file', *MIMETYPES)
        df = _extract_dataframe(file)
        owners = []
        farms = []

        for _, row in df.iterrows():
            try:
                owner_data = _extract_owner(row.to_dict())
                owner_data = owner_schema.load(owner_data)
                owners.append(owner_data)
            except ValidationError as e:
                log.warning(f'Skipped owner {owner_data}. Reason: {e}')
            except KeyError:
                log.warning(f'Missing attribute in row {row.to_dict()}')

        for _, row in df.iterrows():
            try:
                farm_data = _extract_farm(row.to_dict())
                farm_data = farm_schema.load(farm_data)
                farms.append(farm_data)
            except ValidationError as e:
                log.warning(f'Skipped farm {farm_data}. Reason: {e}')
            except KeyError:
                log.warning(f'Missing attribute in row {row.to_dict()}')

        imported_info = service.import_data(owners, farms)
        return jsonify(imported_info)

    return bp
