from dataclasses import dataclass

from .entity import Entity


@dataclass
class CalculatorSettings(Entity):
    '''Fatores e Constantes'''

    # I19 - Óxido Nitroso (N₂O)
    nitrous_oxide: float

    # I20 - Metano (CH₄)
    methane: float

    # I30 - Volatilização N Sintético
    synthetic_n_volatilization: float

    # I31 - Volatilização N Sintético
    volatilization_n_residue: float

    # I32 - Volatilização N Ureia
    urea_n_volatilization: float

    # I33 - Lixiviação/Escoamento superficial
    leaching: float

    # I36 - Slope - Soja
    soy_slope: float

    # I37 - Intercept - Soja
    soy_intercept: float

    # I38 - Nag - Soja
    soy_nag: float

    # I39 - Nbg - Soja
    soy_nbg: float

    # I40 - Rbg-bio - Soja
    soy_rbg_bio: float

    # I41 - Frac dm - Soja
    soy_frac_dm: float

    # I42 - Slope - 2º Safra (Milho)
    corn_slope_second_crop: float

    # I43 - Intercept - 2º Safra (Milho)
    corn_intercept_second_crop: float

    # I44 - Nag - 2º Safra (Milho)
    corn_nag_second_crop: float

    # I45 - Nbg - 2º Safra (Milho)
    corn_nbg_second_crop: float

    # I46 - Rbg-bio - 2º Safra (Milho)
    corn_rbg_bio_second_crop: float

    # I47 - Frac dm - 2º Safra (Milho)
    corn_frac_dm_second_crop: float

    # J50 - Diesel B10
    diesel_b10: float

    # J51 - Gaolina comum
    regular_gasoline: float

    # K60 - Fertilizante sintético
    synthetic_fertilization: float

    # I61 - Ureia CO2
    urea_co2: float

    # K61 - Ureia N2O
    urea_n2o: float

    # K64 - Adubo N Orgânico
    organic_n_fertilizer: float

    # K67 - Adubação verde #1
    green_fertilizer_1: float

    # K68 - Adubação verde #2
    green_fertilizer_2: float

    # K69 - Adubação verde #3
    green_fertilizer_3: float

    # K72 - Volatilização ou Deposição atmosférica
    atmospheric_deposition: float

    # K73 - Lixiviação ou Escoamento superfical
    leaching_n_fertilizer: float

    # I78 - Calcário calcítico
    calcitic_limestone: float

    # I79 - Calcário dolomítico
    dolomitic_limestone: float

    # I80 - Gesso agrícola
    agricultural_plaster: float

    # I90 - Diesel CO2
    diesel_c02_mobile_source: float

    # J90 - Diesel CH4
    diesel_ch4_mobile_source: float

    # K90 - Diesel N2O
    diesel_n2o_mobile_source: float

    # I91 - Diesel CO2
    diesel_c02_stationary_source: float

    # J91 - Diesel CH4
    diesel_ch4_stationary_source: float

    # K91 - Diesel N2O
    diesel_n20_stationary_source: float

    # I92 - Gasolina
    consumption_gasoline: float

    # I103 - Cultivo de solos orgânicos
    organic_soils_cultivation: float

    # K104 - Perda de nitrogênio (N)
    nitrogen_loss: float

    # I109 - Amazônia (Floresta Ombrófila Aberta Terras Baixas)
    preserved_native_forest_soil_1: float

    # I110 - Amazônia (Floresta Ombrófila Aberta Submontana)
    preserved_native_forest_soil_2: float

    # I111 - Amazônia (Floresta Ombrófila Densa Aluvial)
    preserved_native_forest_soil_3: float

    # I112 - Amazônia (Floresta Ombrófila Densa de Terras Baixas)
    preserved_native_forest_soil_4: float

    # I113 - Amazônia (Floresta Ombrófila Densa Submontana)
    preserved_native_forest_soil_5: float

    # I114 - Amazônia (Floresta Estacional Semidecidual Submontana)
    preserved_native_forest_soil_6: float

    # I115 - Amazônia (Floresta Ombrófila Aberta Aluvial)
    preserved_native_forest_soil_7: float

    # I116 - Amazônia (Campinarana Florestada)
    preserved_native_forest_soil_8: float

    # I117 - Amazônia (Vegetação com influência fluvial e/ou lacustre)
    preserved_native_forest_soil_9: float

    # I118 - Amazônia (Savana Arborizada)
    preserved_native_forest_soil_10: float

    # I119 - Amazônia (Savana Florestada)
    preserved_native_forest_soil_11: float

    # I120 - Amazônia (Savana Parque)
    preserved_native_forest_soil_12: float

    # I121 - Cerrado (Savana Arborizada)
    preserved_native_forest_soil_13: float

    # I122 - Cerrado (Savana Florestada (BA-DF-GO-MG))
    preserved_native_forest_soil_14: float

    # I123 - Cerrado (Savana Florestada (MS-MT))
    preserved_native_forest_soil_15: float

    # I124 - Cerrado (Savana Florestada (MA-PI-TO))
    preserved_native_forest_soil_16: float

    # I125 - Cerrado (Savana Gramíneo-lenhosa)
    preserved_native_forest_soil_17: float

    # I126 - Cerrado (Contato Savana/Floresta Estacional)
    preserved_native_forest_soil_18: float

    # I127 - Cerrado (Savana Parque)
    preserved_native_forest_soil_19: float

    # I128 - Cerrado (Floresta Estacional Decidual Montana (BA-GO-MG-PI))
    preserved_native_forest_soil_20: float

    # I129 - Cerrado (Floresta Estacional Decidual Montana (MS-TO))
    preserved_native_forest_soil_21: float

    # I130 - Cerrado (Floresta Estacional Decidual Submontana
    # (BA-GO-MA-MG-PI-TO))
    preserved_native_forest_soil_22: float

    # I131 - Cerrado (Floresta Estacional Decidual Submontana (MS-MT-SP))
    preserved_native_forest_soil_23: float

    # I132 - Cerrado (Floresta Estacional Semidecidual Aluvial (MA-PA-TO))
    preserved_native_forest_soil_24: float

    # I133 - Cerrado (Floresta Estacional Semidecidual Aluvial (BA-GO-MG-PI))
    preserved_native_forest_soil_25: float

    # I134 - Cerrado (Floresta Estacional Semidecidual Aluvial (MS-MT))
    preserved_native_forest_soil_26: float

    # I135 - Cerrado (Floresta Estacional Semidecidual Montana (BA-PI))
    preserved_native_forest_soil_27: float

    # I136 - Cerrado (Floresta Estacional Semidecidual Montana
    # (GO-MG-MS-PR-SP-TO))
    preserved_native_forest_soil_28: float

    # I137 - Cerrado (Floresta Estacional Semidecidual Submontana (BA-MA-PI))
    preserved_native_forest_soil_29: float

    # I138 - Cerrado (Floresta Estacional Semidecidual Submontana
    # (GO/MG/MS/MT/SP/TO))
    preserved_native_forest_soil_30: float

    # I139 - Cerrado (Savana)
    preserved_native_forest_soil_31: float

    # I151 - Compra de energia elétrica (Ano) 2019
    purchase_of_electricity_2019: float

    # I152 - Compra de energia elétrica (Ano) 2020
    purchase_of_electricity_2020: float

    # I167 - Biodiesel CO2
    consumption_biodiesel_co2_mobile_source: float

    # J167 - Biodiesel CH4
    consumption_biodiesel_ch4_mobile_source: float

    # K167 - Biodiesel N20
    consumption_biodiesel_n20_mobile_source: float

    # I170 - Etanol CO2
    consumption_ethanol_co2_stationary_source: float

    # J170 - Etanol CH4
    consumption_ethanol_ch4_stationary_source: float

    # K170 - Etanol N2O
    consumption_ethanol_n20_stationary_source: float

    # I175 - Adubo Verde
    nitrogen_fertilization_green_fertilizer: float

    # J182 - Cultivo Convencional → iLPF (Geral)
    land_occupation_1: float

    # J183 - Cultivo Convencional → Plantio Direto (Demais Regiões)
    land_occupation_2: float

    # J184 - Cultivo Convencional → Plantio Direto (Sul)
    land_occupation_3: float

    # J185 - Pastagem Degradada → Cultivo Convencional (Geral)
    land_occupation_4: float

    # J186 - Pastagem Degradada → iLPF (Geral)
    land_occupation_5: float

    # J187 - Pastagem Degradada → Plantio Direto (Geral)
    land_occupation_6: float

    # J188 - Pastagem/Pastagem melhorada → iLPF (Geral)
    land_occupation_7: float

    # J189 - Plantio Direto → Cultivo Convencional (Geral)
    land_occupation_8: float

    # J190 - Plantio Direto → iLPF (Geral)
    land_occupation_9: float

    # J191 - Floresta Nativa → Cultivo Convencional (Argila > 60%)
    land_occupation_10: float

    # J192 - Floresta Nativa → Cultivo Convencional (Argila < 60%)
    land_occupation_11: float

    # J193 - Floresta Nativa → iLPF (Geral)
    land_occupation_12: float

    # J194 - Floresta Nativa → Plantio Direto (Amazônia)
    land_occupation_13: float

    # J195 - Floresta Nativa → Plantio Direto (Cerrado)
    land_occupation_14: float

    # J196 - Floresta Nativa → Pastagem Degradada
    land_occupation_15: float

    # J197 - Floresta Nativa → Pastagem Nominal
    land_occupation_16: float

    # J198 - Floresta Nativa → Pastagem Melhorada
    land_occupation_17: float

    # J201 - Sistema de Plantio Direto (SPD) - Uso de cobertura
    no_tillage_system_coverage: float

    # J202 - Sistema de Plantio Direto (SPD)
    no_tillage_system: float

    # J203 - Sistema de Plantio Convencional (SPC)
    conventional_planting_system: float

    @classmethod
    def create_default(cls):
        return cls.new(
            dict(
                nitrous_oxide=265,
                synthetic_n_volatilization=0.11,
                volatilization_n_residue=0.21,
                urea_n_volatilization=0.15,
                leaching=0.24,
                synthetic_fertilization=0.0113,
                urea_co2=0.733,
                urea_n2o=0.0088,
                organic_n_fertilizer=0.0113,
                atmospheric_deposition=0.01,
                leaching_n_fertilizer=0.0075,
                calcitic_limestone=0.44,
                dolomitic_limestone=0.47667,
                purchase_of_electricity_2019=0.075,
                purchase_of_electricity_2020=0.0617,
                no_tillage_system_coverage=-1.76,
                no_tillage_system=-1.53,
                conventional_planting_system=0.877,
                agricultural_plaster=0.4,
                soy_slope=0.93,
                soy_frac_dm=0.87,
                soy_intercept=1.35,
                soy_nag=0.009,
                soy_nbg=0.009,
                soy_rbg_bio=0.11,
                regular_gasoline=0.73,
                diesel_b10=0.9,
                consumption_gasoline=0.002212,
                diesel_c02_mobile_source=2.603,
                diesel_ch4_mobile_source=0.0001,
                diesel_n2o_mobile_source=0.00014,
                diesel_c02_stationary_source=2.6,
                diesel_ch4_stationary_source=0.00036,
                diesel_n20_stationary_source=0.000021,
                methane=28,
                organic_soils_cultivation=73.3333333333333,
                nitrogen_loss=0.0188571428571429,
                green_fertilizer_1=0.000382380952380952,
                green_fertilizer_2=0.000158015873015873,
                green_fertilizer_3=0.000247761904761905,
                consumption_biodiesel_co2_mobile_source=2.431,
                consumption_biodiesel_ch4_mobile_source=0.0003,
                consumption_biodiesel_n20_mobile_source=0.00002,
                consumption_ethanol_co2_stationary_source=1.5,
                consumption_ethanol_ch4_stationary_source=0.00021,
                consumption_ethanol_n20_stationary_source=0.000013,
                nitrogen_fertilization_green_fertilizer=1.84,
                corn_slope_second_crop=1.03,
                corn_intercept_second_crop=0.61,
                corn_nag_second_crop=0.007,
                corn_nbg_second_crop=0.014,
                corn_rbg_bio_second_crop=0.21,
                corn_frac_dm_second_crop=0.87,
                land_occupation_1=-6.2333,
                land_occupation_2=-1.76,
                land_occupation_3=-1.2833,
                land_occupation_4=0.9167,
                land_occupation_5=-1.7,
                land_occupation_6=-0.6967,
                land_occupation_7=-3.666,
                land_occupation_8=0.9167,
                land_occupation_9=-1.0267,
                land_occupation_10=0.1613,
                land_occupation_11=0.9167,
                land_occupation_12=-0.7077,
                land_occupation_13=0.88,
                land_occupation_14=-0.44,
                land_occupation_15=0.649,
                land_occupation_16=1.122,
                land_occupation_17=1.386,
                preserved_native_forest_soil_1=165.900,
                preserved_native_forest_soil_2=132.000,
                preserved_native_forest_soil_3=130.700,
                preserved_native_forest_soil_4=185.300,
                preserved_native_forest_soil_5=201.100,
                preserved_native_forest_soil_6=88.900,
                preserved_native_forest_soil_7=145.300,
                preserved_native_forest_soil_8=131.600,
                preserved_native_forest_soil_9=58.200,
                preserved_native_forest_soil_10=173.100,
                preserved_native_forest_soil_11=150.000,
                preserved_native_forest_soil_12=114.000,
                preserved_native_forest_soil_13=41.310,
                preserved_native_forest_soil_14=52.290,
                preserved_native_forest_soil_15=103.210,
                preserved_native_forest_soil_16=49.640,
                preserved_native_forest_soil_17=18.490,
                preserved_native_forest_soil_18=68.500,
                preserved_native_forest_soil_19=26.790,
                preserved_native_forest_soil_20=51.940,
                preserved_native_forest_soil_21=127.540,
                preserved_native_forest_soil_22=69.010,
                preserved_native_forest_soil_23=127.540,
                preserved_native_forest_soil_24=65.640,
                preserved_native_forest_soil_25=75.860,
                preserved_native_forest_soil_26=167.460,
                preserved_native_forest_soil_27=82.610,
                preserved_native_forest_soil_28=67.760,
                preserved_native_forest_soil_29=54.930,
                preserved_native_forest_soil_30=83.480,
                preserved_native_forest_soil_31=51.630,
            )
        )
