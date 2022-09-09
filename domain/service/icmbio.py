import logging
from typing import List

from domain.model import (
    Geopark,
    EcoCorridors,
    GeoSites,
    IndigenousLand,
    ConservationUnit
)
from domain.repository import IIcmbioRepository


class IcmbioService:
    def __init__(self, repo: IIcmbioRepository):
        self._repo = repo
        self._log = logging.getLogger(self.__class__.__name__)

    def search_geopark(self, filter: dict) -> List[Geopark]:
        return self._repo.find(Geopark, filter)

    def search_ecocorridors(self, filter: dict) -> List[EcoCorridors]:
        return self._repo.find(EcoCorridors, filter)

    def search_geosite(self, filter: dict) -> List[GeoSites]:
        return self._repo.find(GeoSites, filter)

    def search_indigenousland(self, filter: dict) -> List[IndigenousLand]:
        return self._repo.find(IndigenousLand, filter)

    def search_consvunit(self, filter: dict) -> List[ConservationUnit]:
        return self._repo.find(ConservationUnit, filter)

    def save_geopark(self, data: dict) -> Geopark:
        unit = self._repo.find_by_imported_id(Geopark, data['imported_id'])

        if unit is None:
            unit = self._repo.add(Geopark, Geopark.new(data))
            self._log.debug(f'Added unit {unit._id}')
        else:
            self._repo.update(Geopark, unit.merge(data))
            self._log.debug(f'Updated unit {unit._id}')

        return unit

    def save_ecocorridor(self, data: dict) -> EcoCorridors:
        unit = self._repo.find_by_imported_id(
            EcoCorridors, data['imported_id']
        )

        if unit is None:
            unit = self._repo.add(EcoCorridors, EcoCorridors.new(data))
            self._log.debug(f'Added unit {unit._id}')
        else:
            self._repo.update(EcoCorridors, unit.merge(data))
            self._log.debug(f'Updated unit {unit._id}')

        return unit

    def save_geosite(self, data: dict) -> GeoSites:
        unit = self._repo.find_by_imported_id(GeoSites, data['imported_id'])

        if unit is None:
            unit = self._repo.add(GeoSites, GeoSites.new(data))
            self._log.debug(f'Added unit {unit._id}')
        else:
            self._repo.update(GeoSites, unit.merge(data))
            self._log.debug(f'Updated unit {unit._id}')

        return unit

    def save_indigenousland(self, data: dict) -> IndigenousLand:
        unit = self._repo.find_by_imported_id(
            IndigenousLand, data['imported_id']
        )

        if unit is None:
            unit = self._repo.add(IndigenousLand, IndigenousLand.new(data))
            self._log.debug(f'Added unit {unit._id}')
        else:
            self._repo.update(IndigenousLand, unit.merge(data))
            self._log.debug(f'Updated unit {unit._id}')

        return unit

    def save_conservation_unit(self, data: dict) -> ConservationUnit:
        unit = self._repo.find_by_imported_id(
            ConservationUnit, data['imported_id']
        )

        if unit is None:
            unit = self._repo.add(ConservationUnit, ConservationUnit.new(data))
            self._log.debug(f'Added unit {unit._id}')
        else:
            self._repo.update(ConservationUnit, unit.merge(data))
            self._log.debug(f'Updated unit {unit._id}')

        return unit
