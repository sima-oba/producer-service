import logging
import json
from typing import List

from domain.model import Farm, Owner, ImportInfo
from domain.exception import EntityNotFoundError
from domain.repository import IFarmRepository, IPublisher


class FarmService:
    def __init__(self, repo: IFarmRepository, pub: IPublisher):
        self._repo = repo
        self._pub = pub
        self._log = logging.getLogger(self.__class__.__name__)

    def summary_farms(self, filter: dict = None) -> List[dict]:
        return self._repo.summary_farms(filter)

    def search_farms(self, filter: dict = None) -> List[Farm]:
        return self._repo.search_farms(filter)

    def get_farms(self, ids: List[str]) -> List[Farm]:
        return self._repo.find_farms_by_ids(ids)

    def get_farm(self, _id: str) -> Farm:
        farm = self._repo.find_farm_by_id(_id)

        if farm is None:
            raise EntityNotFoundError(Farm, f'_id {_id}')

        return farm

    def add_farm(self, data: dict) -> Farm:
        owner = self._repo.find_owner_by_doc(data['owner_doc'])

        if owner is None:
            raise EntityNotFoundError(Owner, f'{data["owner_doc"]}')

        farm = self._repo.find_farm_by_code(data['farm_code'])

        if farm is None:
            farm = Farm.new(data)
            farm = self._repo.add_farm(farm)
            self._log.debug(f'added farm {farm._id}')
        else:
            farm = farm.merge(data)
            farm = self._repo.update_farm(farm)
            self._log.debug(f'updated farm {farm._id}')

        return farm

    def update_farm_info(self, data: dict, _id: str) -> Farm:
        farm = self.get_farm(_id)
        farm = farm.merge(data)
        self._repo.update_farm(farm)
        self._log.debug(f'updated farm info {farm._id}')

        return farm

    def get_owners(self) -> List[Owner]:
        return self._repo.find_owners()

    def get_owner_by_id(self, _id: str) -> Owner:
        owner = self._repo.find_owner_by_id(_id)

        if owner is None:
            raise EntityNotFoundError(Owner, f'_id {_id}')

        return owner

    def add_owner(self, data: dict) -> Owner:
        owner = self._repo.find_owner_by_doc(data['doc'])

        if owner is None:
            owner = Owner.new(data)
            self._repo.add_owner(owner)
            self._log.debug(f'added owner {owner.doc}')
        else:
            owner = owner.merge(data)
            self._repo.update_owner(owner)
            self._log.debug(f'updated owner {owner.doc}')

        data['defaulting'] = "False"
        data['_id'] = owner._id

        self._pub.send(
            topic='NEW_OWNER',
            data=json.dumps(data, ensure_ascii=False),
            key=data['doc']
        )

        return owner

    def import_data(self, owners: List[dict], farms: List[dict]) -> ImportInfo:
        imported_owners = set()
        imported_farms = set()

        for owner_data in owners:
            owner = self.add_owner(owner_data)
            imported_owners.add(owner.doc)

        for farm_data in farms:
            try:
                farm = self.add_farm(farm_data)
                imported_farms.add(farm.farm_code)
            except EntityNotFoundError as e:
                self._log.warn(
                    f'Failed to import farm {farm.farm_code}. Reason: {e}'
                )

        import_info = ImportInfo.new({
            'imported_owners': len(imported_owners),
            'imported_farms': len(imported_farms)
        })
        self._repo.add_imported_info(import_info)

        return import_info

    def get_imported_info(self) -> List[ImportInfo]:
        return self._repo.find_imported_info()
