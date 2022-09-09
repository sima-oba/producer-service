from dataclasses import dataclass
from datetime import datetime


@dataclass
class CalculatorDataCollect:
    '''Coleta de Dados da Atividade'''

    farm_id: str
    farm_name: str
    resp_name: str
    organization: str
    date: datetime


    # E32 - Área de cultivo
    cultivated_area: float

    # E34 - Irrigação da Soja
    coverage_use: float

    crop_year: str

    crop_year_second: bool

    # E37 - Área de cultivo 2º Safra
    cultivated_area_second_crop: float

    # C39 - Bioma #1
    biome_1: float

    # F39 - Abrangência do Bioma
    biome_1_coverage: bool

    # C40 - Bioma #2
    biome_2: float

    # F40 - Abrangência do Bioma
    biome_2_coverage: bool

    # C41 - Bioma #3
    biome_3: float

    # F41 - Abrangência do Bioma
    biome_3_coverage: bool

    # E48 - Produtividade média
    average_productivity: float

    # L48 - Produtividade média
    average_productivity_second_crop: float

    # B50 - Sistema de Cultivo
    cultivation_system: float

    # E57 - Área de solos orgânicos
    area_organic_soils: float

    # E63 - Adubo N Sintético: Tipo 1
    synthetic_n_fertilizer_type1_kg: float

    # F63 - Adubo N Sintético: Tipo 2
    synthetic_n_fertilizer_type2_kg: float

    # G63 - Adubo N Sintético: Tipo 3
    synthetic_n_fertilizer_type3_kg: float

    # L63 - Adubo N Sintético: Tipo 1
    synthetic_n_fertilizer_type1_kg_second_crop: float

    # M63 - Adubo N Sintético: Tipo 2
    synthetic_n_fertilizer_type2_kg_second_crop: float

    # N63 - Adubo N Sintético: Tipo 3
    synthetic_n_fertilizer_type3_kg_second_crop: float

    # E64 - Teor N adubo sintético: Tipo 1
    synthetic_n_fertilizer_teor_type1: float

    # F64 - Teor N adubo sintético: Tipo 2
    synthetic_n_fertilizer_teor_type2: float

    # G64 - Teor N adubo sintético: Tipo 3
    synthetic_n_fertilizer_teor_type3: float

    # L64 - Teor N adubo sintético: Tipo 1
    synthetic_n_fertilizer_teor_type1_second_crop: float

    # M64 - Teor N adubo sintético: Tipo 2
    synthetic_n_fertilizer_teor_type2_second_crop: float

    # N64 - Teor N adubo sintético: Tipo 3
    synthetic_n_fertilizer_teor_type3_second_crop: float

    # E65 - Ureia
    urea_type1: int

    # L65 - Ureia
    urea_type1_second_crop: int

    # E68 - Adubo N Orgânico
    organic_n_fertilizer_type1_kg: float

    # L68 - Adubo N Orgânico
    organic_n_fertilizer_type1_kg_second_crop: float

    # E71 - Leguminosa
    green_adubation: float

    # L71 - Leguminosa
    green_adubation_second_crop: float

    # E72 - Gramínea
    grassy_type1_kg: float

    # L72 - Gramínea
    grassy_type1_kg_second_crop: float

    # E73 - Outros
    others_type1_kg: float

    # L73 - Outros
    others_type1_kg_second_crop: float

    # E78 - Calcário calcítico
    calcitic_limestone: float

    # L78 - Calcário calcítico
    calcitic_limestone_second_crop: float

    # E79 - Calcário dolomítico
    dolomitic_limestone: float

    # L79 - Calcário dolomítico
    dolomitic_limestone_second_crop: float

    # E80 - Gesso agrícola
    agricultural_plaster: float

    # L80 - Gesso agrícola
    agricultural_plaster_second_crop: float

    # L87 - Resíduos no campo
    waste_field_second_crop: float

    # E87 - Resíduos no campo
    waste_field: float

    # E92 - Gasolina
    gasoline_mechanical_operation: float

    # E93 - Diesel
    diesel_b10_mechanical_operation: float

    # E95 - Etanol hidratado
    hydrous_ethanol_mechanical_operation: float

    # E97 - Gasolina
    gasoline_stationary_operation: float

    # E98 - Diesel
    diesel_b10_stationary_operation: float

    # E100 - Etanol hidratado
    hydrous_ethanol_stationary_operation: float

    # E102 - Diesel
    transport_production_diesel_b10: float

    # E107 - Consumo energia
    energy_consumption: float

    # E112 - RL
    rl: float

    # E113 - APP
    app: float

    # E114 - Excedente Florestal
    forest_surplus: float
