from domain.exception import InvalidValueError
from domain.model import PracticeType
from domain.repository import IPracticeRepository


class PracticeReport:
    def __init__(self, repo: IPracticeRepository):
        self._repo = repo
        self._report_methods = {
            PracticeType.CORRECTIVE_QUALITY.value: self._get_corrective_quality, # noqa
            PracticeType.CROP_ROTATION.value: self._get_crop_rotation,
            PracticeType.IRRIGATION_USE_EFFICIENCY.value: self._get_irrigation_use_efficiency,  # noqa
            PracticeType.PHYTOSANITARY.value: self._get_phytosanitary,
            PracticeType.SUSTAINABLE.value: self._get_sustainable,
            PracticeType.WATER_RUNOFF_CONTAINMENT.value: self._get_water_runoff_containment,  # noqa
        }

    def get_totals(self, **kwargs) -> dict:
        period = self._create_period(**kwargs)
        report = {}

        for type in PracticeType:
            count = self._repo.count('practice_type', type.name, period)
            report[type.name] = count

        return report

    def get_report(self, practice_type: PracticeType, **kwargs) -> dict:
        period = self._create_period(**kwargs)
        method = self._report_methods.get(practice_type)
        print(type(practice_type))

        if method is None:
            raise InvalidValueError(f'Unavailable report for {practice_type}')

        return method(period)

    def _get_corrective_quality(self, period) -> dict:
        type = PracticeType.CORRECTIVE_QUALITY
        fields = [
            'is_density_adequate',
            'is_conditioning_adequate',
            'has_declared_elements',
            'is_contaminated',
            'has_logistical_problems'
        ]

        report = {}

        for field in fields:
            report[field] = {
                'yes': self._repo.count(field, True, period, type),
                'no': self._repo.count(field, False, period, type)
            }

        return report

    def _get_crop_rotation(self, period) -> dict:
        type = PracticeType.CROP_ROTATION
        crops = [
            'algodao',
            'milho',
            'soja',
            'cafe',
            'trigo',
            'feijao',
            'milheto',
            'sorgo',
            'outras'
        ]

        report = {}

        for crop in crops:
            report[crop] = self._repo.count('crops', crop, period, type)

        return report

    def _get_irrigation_use_efficiency(self, period) -> dict:
        type = PracticeType.IRRIGATION_USE_EFFICIENCY
        fields = [
            'has_irrigated_agriculturearea',
            'has_flow_meter',
            'meter_transmits_telemetric_data',
            'use_of_irrigation_systems'
        ]

        report = {}

        for field in fields:
            report[field] = {
                'yes': self._repo.count(field, True, period, type),
                'no': self._repo.count(field, False, period, type)
            }

        return report

    def _get_phytosanitary(self, period) -> dict:
        type = PracticeType.PHYTOSANITARY
        fields = [
            'uses_agronomic_management',
            'uses_refuge',
            'uses_precision_systems',
            'uses_mip',
            'uses_mid'
        ]

        report = {}

        for field in fields:
            report[field] = {
                'yes': self._repo.count(field, True, period, type),
                'no': self._repo.count(field, False, period, type)
            }

        return report

    def _get_sustainable(self, period) -> dict:
        type = PracticeType.SUSTAINABLE
        yes_no_fields = [
            'are_satisfied_with_planting',
            'perform_agricultural_operations',
            'has_terraces',
            'has_erosion',
            'has_soil_disturbance',
            'is_soil_compactated',
            'has_earthworms',
            'are_earthworms_good_for_crops',
            'follow_technical_guidelines',
            'uses_manure'
        ]

        report = {}

        for field in yes_no_fields:
            report[field] = {
                'yes': self._repo.count(field, True, period, type),
                'no': self._repo.count(field, False, period, type)
            }

        report['planting_assessment'] = {}

        for val in range(4):
            count = self._repo.count('planting_assessment', val, period, type)
            report['planting_assessment'][val] = count

        return report

    def _get_water_runoff_containment(self, period) -> dict:
        type = PracticeType.WATER_RUNOFF_CONTAINMENT
        yes_no_fields = [
            'has_micro_dams',
            'has_level_curves',
            'level_curves_convergent_with_neighbors'
        ]

        report = {}

        for field in yes_no_fields:
            report[field] = {
                'yes': self._repo.count(field, True, period, type),
                'no': self._repo.count(field, False, period, type)
            }

        report['micro_dams_quality'] = {}

        for val in range(4):
            count = self._repo.count('micro_dams_quality', val, period, type)
            report['micro_dams_quality'][val] = count

        report['level_curves_quality'] = {}

        for val in range(4):
            count = self._repo.count('level_curves_quality', val, period, type)
            report['level_curves_quality'][val] = count

        return report

    def _create_period(self, **kwargs):
        start = kwargs.get('start')
        end = kwargs.get('end')

        if start and end:
            return start, end

        return None
