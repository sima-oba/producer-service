from dataclasses import is_dataclass

from flask import Response, make_response
from orjson import dumps


def export_feature_collection(data: list, key: str = 'geometry') -> dict:
    if not data:
        return {
            'type': 'FeatureCollection',
            'features': []
        }

    features = []

    for index, feat in enumerate(data):
        if is_dataclass(feat):
            feat = feat.__dict__

        geometry = feat.pop(key, None)

        features.append({
            'id': index,
            'type': 'Feature',
            'properties': {key: value for key, value in feat.items()},
            'geometry': geometry
        })

    return {
        'type': 'FeatureCollection',
        'features': features
    }


def make_geojson_response(content: list) -> Response:
    resp = make_response()
    resp.content_type = 'application/json'
    resp.status_code = 200
    resp.data = dumps(export_feature_collection(content))

    return resp
