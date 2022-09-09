from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .base import BasePractice, Evaluation


@dataclass
class SustainableEval(Evaluation):
    are_satisfied_with_planting: bool
    planting_assessment: bool
    planting_difficulties: bool
    planting_years: bool
    planting_importance: bool
    perform_agricultural_operations: bool
    has_terraces: bool
    has_erosion: bool
    has_soil_disturbance: bool
    is_soil_compactated: bool
    soil_preparation_frequency: bool
    bare_soil_months: bool
    summer_crops: bool
    winter_crops: bool
    animals_on_plating_area: bool
    has_earthworms: bool
    are_earthworms_different: bool
    are_earthworms_good_for_crops: bool
    earthworms_consequence_for_crops: bool
    fertilizing_type: bool
    follow_technical_guidelines: bool
    uses_manure: bool
    manure_per_year: bool
    no_soil_preparation_start: bool
    no_soil_preparation_end: bool
    soil_management_start: bool
    soil_management_end: bool
    dry_material_accumulation_start: bool
    dry_material_accumulation_end: bool
    dry_material_accumulation_tons: bool


@dataclass
class SustainablePractice(BasePractice):
    are_satisfied_with_planting: bool
    planting_assessment: int
    planting_difficulties: str
    planting_years: int
    planting_importance: str
    perform_agricultural_operations: bool
    has_terraces: bool
    has_erosion: bool
    has_soil_disturbance: bool
    is_soil_compactated: bool
    soil_preparation_frequency: str
    bare_soil_months: int
    summer_crops: List[str]
    winter_crops: List[str]
    animals_on_plating_area: str
    has_earthworms: bool
    are_earthworms_different: Optional[int]
    are_earthworms_good_for_crops: Optional[bool]
    earthworms_consequence_for_crops: str
    fertilizing_type: str
    follow_technical_guidelines: bool
    uses_manure: bool
    manure_per_year: Optional[int]
    no_soil_preparation_start: datetime
    no_soil_preparation_end: datetime
    soil_management_start: datetime
    soil_management_end: datetime
    dry_material_accumulation_start: datetime
    dry_material_accumulation_end: datetime
    dry_material_accumulation_tons: float
    evaluation: Optional[SustainableEval]
