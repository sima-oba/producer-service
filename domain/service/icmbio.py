import logging
from typing import List

from domain.model import (
    AtlanticForest,
    Biome,
    Geopark,
    EcoCorridors,
    GeoSites,
    IndigenousLand,
    ConservationUnit,
    Matopiba,
    Vegetation
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

    def search_atlantic_forest(self) -> List[AtlanticForest]:
        return self._repo.find(AtlanticForest)

    def search_biomes(self) -> List[Biome]:
        return self._repo.find(Biome)

    def search_matopiba(self) -> List[Matopiba]:
        return self._repo.find(Matopiba)

    def search_vegetation(self) -> List[Vegetation]:
        return self._repo.find(Vegetation)

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

    def save_atlantic_forest(self, data: dict) -> AtlanticForest:
        forest = self._repo.find_by_imported_id(
            AtlanticForest, data['imported_id_0']
        )

        if forest is None:
            forest = self._repo.add(AtlanticForest, AtlanticForest.new(data))
            self._log.debug(f'Added forest {forest._id}')
        else:
            self._repo.update(AtlanticForest, forest.merge(data))
            self._log.debug(f'Updated forest {forest._id}')

        return forest

    def save_biome(self, data: dict) -> Biome:
        biome = self._repo.find_by_imported_id(
            Biome, data['imported_id']
        )

        if biome is None:
            biome = self._repo.add(Biome, Biome.new(data))
            self._log.debug(f'Added biome {biome._id}')
        else:
            self._repo.update(Biome, biome.merge(data))
            self._log.debug(f'Updated biome {biome._id}')

        return biome

    def save_matopiba(self, data: dict) -> Matopiba:
        matopiba = self._repo.find_by_imported_id(
            Matopiba, data['state']
        )

        if matopiba is None:
            matopiba = self._repo.add(Matopiba, Matopiba.new(data))
            self._log.debug(f'Added Matopiba {matopiba._id}')
        else:
            self._repo.update(Matopiba, matopiba.merge(data))
            self._log.debug(f'Updated Matopiba {matopiba._id}')

        return matopiba

    
    def save_vegetation(self, data: dict) -> Vegetation:
        vegetation = self._repo.find_by_imported_id(
            Vegetation, data['imported_id']
        )

        if vegetation is None:
            vegetation = self._repo.add(Vegetation, Vegetation.new(data))
            self._log.debug(f'Added Vegetation {vegetation._id}')
        else:
            self._repo.update(Vegetation, vegetation.merge(data))
            self._log.debug(f'Updated Vegetation {vegetation._id}')

        return vegetation
