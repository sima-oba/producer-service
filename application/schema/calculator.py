from marshmallow import Schema, fields, EXCLUDE, post_load


class GeneralInfo(Schema):
    class Meta:
        unknown = EXCLUDE
    farm_id = fields.String(required=True)
    resp_name = fields.String(required=True)
    organization = fields.String(required=True)
    date = fields.DateTime(required=True)


class FarmInfo(Schema):
    class Meta:
        unknown = EXCLUDE
    cultivated_area = fields.Float(required=True)
    coverage_use = fields.Float(required=True)
    crop_year = fields.String(required=True)
    crop_year_second = fields.Boolean(missing=None)
    cultivated_area_second_crop = fields.Float(required=True)
    biome_1 = fields.Float(required=True)
    biome_1_coverage = fields.Boolean(required=True)
    biome_2 = fields.Float(required=True)
    biome_2_coverage = fields.Boolean(required=True)
    biome_3 = fields.Float(required=True)
    biome_3_coverage = fields.Boolean(required=True)


class CultivationSystem(Schema):
    class Meta:
        unknown = EXCLUDE
    average_productivity = fields.Float(required=True)
    average_productivity_second_crop = fields.Float(required=True)
    cultivation_system = fields.Float(required=True)


class SoilCharacteristics(Schema):
    class Meta:
        unknown = EXCLUDE
    area_organic_soils = fields.Float(required=True)


class NitroFertilization(Schema):
    class Meta:
        unknown = EXCLUDE
    synthetic_n_fertilizer_type1_kg = fields.Float(required=True)
    synthetic_n_fertilizer_type2_kg = fields.Float(required=True)
    synthetic_n_fertilizer_type3_kg = fields.Float(required=True)
    synthetic_n_fertilizer_type1_kg_second_crop = fields.Float(required=True)
    synthetic_n_fertilizer_type2_kg_second_crop = fields.Float(required=True)
    synthetic_n_fertilizer_type3_kg_second_crop = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type1 = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type2 = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type3 = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type1_second_crop = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type2_second_crop = fields.Float(required=True)
    synthetic_n_fertilizer_teor_type3_second_crop = fields.Float(required=True)
    urea_type1 = fields.Integer(required=True)
    urea_type1_second_crop = fields.Integer(required=True)
    organic_n_fertilizer_type1_kg = fields.Float(required=True)
    organic_n_fertilizer_type1_kg_second_crop = fields.Float(required=True)
    green_adubation = fields.Float(required=True)
    green_adubation_second_crop = fields.Float(required=True)
    grassy_type1_kg = fields.Float(required=True)
    grassy_type1_kg_second_crop = fields.Float(required=True)
    others_type1_kg = fields.Float(required=True)
    others_type1_kg_second_crop = fields.Float(required=True)

    @post_load
    def convert(self, data: dict, **_):
        data['synthetic_n_fertilizer_teor_type1'] = (
            data['synthetic_n_fertilizer_teor_type1'] * 0.01
        )

        data['synthetic_n_fertilizer_teor_type2'] = (
            data['synthetic_n_fertilizer_teor_type2'] * 0.01
        )

        data['synthetic_n_fertilizer_teor_type3'] = (
            data['synthetic_n_fertilizer_teor_type3'] * 0.01
        )

        data['synthetic_n_fertilizer_teor_type1_second_crop'] = (
            data['synthetic_n_fertilizer_teor_type1_second_crop'] * 0.01
        )

        data['synthetic_n_fertilizer_teor_type2_second_crop'] = (
            data['synthetic_n_fertilizer_teor_type2_second_crop'] * 0.01
        )

        data['synthetic_n_fertilizer_teor_type3_second_crop'] = (
            data['synthetic_n_fertilizer_teor_type3_second_crop'] * 0.01
        )

        return data


class SoilCorrection(Schema):
    class Meta:
        unknown = EXCLUDE
    calcitic_limestone = fields.Float(required=True)
    calcitic_limestone_second_crop = fields.Float(required=True)
    dolomitic_limestone = fields.Float(required=True)
    dolomitic_limestone_second_crop = fields.Float(required=True)
    agricultural_plaster = fields.Float(required=True)
    agricultural_plaster_second_crop = fields.Float(required=True)


class Decomposition(Schema):
    class Meta:
        unknown = EXCLUDE
    waste_field = fields.Float(required=True)
    waste_field_second_crop = fields.Float(required=True)

    @post_load
    def covert(self, data: dict, **_):
        data['waste_field'] = (
            data['waste_field'] * 0.01
        )

        data['waste_field_second_crop'] = (
            data['waste_field_second_crop'] * 0.01
        )

        return data


class FuelConsumpiton(Schema):
    class Meta:
        unknown = EXCLUDE
    gasoline_mechanical_operation = fields.Float(required=True)
    diesel_b10_mechanical_operation = fields.Float(required=True)
    gasoline_stationary_operation = fields.Float(required=True)
    diesel_b10_stationary_operation = fields.Float(required=True)
    hydrous_ethanol_mechanical_operation = fields.Float(required=True)
    hydrous_ethanol_stationary_operation = fields.Float(required=True)
    transport_production_diesel_b10 = fields.Float(required=True)


class Stock(Schema):
    class Meta:
        unknown = EXCLUDE
    rl = fields.Float(required=True)
    app = fields.Float(required=True)
    forest_surplus = fields.Float(required=True)


class CalculatorDataCollectSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    general_info = fields.Nested(GeneralInfo, required=True)
    farm_info = fields.Nested(FarmInfo, required=True)
    cultivation_system = fields.Nested(CultivationSystem, required=True)
    soil_characteristics = fields.Nested(SoilCharacteristics, required=True)
    nitrogen_fertilization = fields.Nested(NitroFertilization, required=True)
    correction = fields.Nested(SoilCorrection, required=True)
    decomposition = fields.Nested(Decomposition, required=True)
    fuel_consumption = fields.Nested(FuelConsumpiton, required=True)
    energy_consumption = fields.Float(required=True)
    stock = fields.Nested(Stock, required=True)

    @post_load
    def format(self, payload: dict, **_):
        return {
            **payload['general_info'],
            **payload['farm_info'],
            **payload['cultivation_system'],
            **payload['soil_characteristics'],
            **payload['nitrogen_fertilization'],
            **payload['correction'],
            **payload['decomposition'],
            **payload['fuel_consumption'],
            **payload['stock'],
            'energy_consumption': payload['energy_consumption']
        }


class CalculatorSettingsSchema(Schema):
    nitrous_oxide = fields.Float(required=True)
    methane = fields.Float(required=True)
    synthetic_n_volatilization = fields.Float(required=True)
    volatilization_n_residue = fields.Float(required=True)
    urea_n_volatilization = fields.Float(required=True)
    leaching = fields.Float(required=True)
    soy_slope = fields.Float(required=True)
    soy_intercept = fields.Float(required=True)
    soy_nag = fields.Float(required=True)
    soy_nbg = fields.Float(required=True)
    soy_rbg_bio = fields.Float(required=True)
    soy_frac_dm = fields.Float(required=True)
    corn_slope_second_crop = fields.Float(required=True)
    corn_intercept_second_crop = fields.Float(required=True)
    corn_nag_second_crop = fields.Float(required=True)
    corn_nbg_second_crop = fields.Float(required=True)
    corn_rbg_bio_second_crop = fields.Float(required=True)
    corn_frac_dm_second_crop = fields.Float(required=True)
    diesel_b10 = fields.Float(required=True)
    regular_gasoline = fields.Float(required=True)
    synthetic_fertilization = fields.Float(required=True)
    urea_co2 = fields.Float(required=True)
    urea_n2o = fields.Float(required=True)
    organic_n_fertilizer = fields.Float(required=True)
    green_fertilizer_1 = fields.Float(required=True)
    green_fertilizer_2 = fields.Float(required=True)
    green_fertilizer_3 = fields.Float(required=True)
    atmospheric_deposition = fields.Float(required=True)
    leaching_n_fertilizer = fields.Float(required=True)
    calcitic_limestone = fields.Float(required=True)
    dolomitic_limestone = fields.Float(required=True)
    agricultural_plaster = fields.Float(required=True)
    diesel_c02_mobile_source = fields.Float(required=True)
    diesel_ch4_mobile_source = fields.Float(required=True)
    diesel_n2o_mobile_source = fields.Float(required=True)
    diesel_c02_stationary_source = fields.Float(required=True)
    diesel_ch4_stationary_source = fields.Float(required=True)
    diesel_n20_stationary_source = fields.Float(required=True)
    consumption_gasoline = fields.Float(required=True)
    organic_soils_cultivation = fields.Float(required=True)
    nitrogen_loss = fields.Float(required=True)
    preserved_native_forest_soil_1 = fields.Float(required=True)
    preserved_native_forest_soil_2 = fields.Float(required=True)
    preserved_native_forest_soil_3 = fields.Float(required=True)
    preserved_native_forest_soil_4 = fields.Float(required=True)
    preserved_native_forest_soil_5 = fields.Float(required=True)
    preserved_native_forest_soil_6 = fields.Float(required=True)
    preserved_native_forest_soil_7 = fields.Float(required=True)
    preserved_native_forest_soil_8 = fields.Float(required=True)
    preserved_native_forest_soil_9 = fields.Float(required=True)
    preserved_native_forest_soil_10 = fields.Float(required=True)
    preserved_native_forest_soil_11 = fields.Float(required=True)
    preserved_native_forest_soil_12 = fields.Float(required=True)
    preserved_native_forest_soil_13 = fields.Float(required=True)
    preserved_native_forest_soil_14 = fields.Float(required=True)
    preserved_native_forest_soil_15 = fields.Float(required=True)
    preserved_native_forest_soil_16 = fields.Float(required=True)
    preserved_native_forest_soil_17 = fields.Float(required=True)
    preserved_native_forest_soil_18 = fields.Float(required=True)
    preserved_native_forest_soil_19 = fields.Float(required=True)
    preserved_native_forest_soil_20 = fields.Float(required=True)
    preserved_native_forest_soil_21 = fields.Float(required=True)
    preserved_native_forest_soil_22 = fields.Float(required=True)
    preserved_native_forest_soil_23 = fields.Float(required=True)
    preserved_native_forest_soil_24 = fields.Float(required=True)
    preserved_native_forest_soil_25 = fields.Float(required=True)
    preserved_native_forest_soil_26 = fields.Float(required=True)
    preserved_native_forest_soil_27 = fields.Float(required=True)
    preserved_native_forest_soil_28 = fields.Float(required=True)
    preserved_native_forest_soil_29 = fields.Float(required=True)
    preserved_native_forest_soil_30 = fields.Float(required=True)
    preserved_native_forest_soil_31 = fields.Float(required=True)
    purchase_of_electricity_2019 = fields.Float(required=True)
    purchase_of_electricity_2020 = fields.Float(required=True)
    consumption_biodiesel_co2_mobile_source = fields.Float(required=True)
    consumption_biodiesel_ch4_mobile_source = fields.Float(required=True)
    consumption_biodiesel_n20_mobile_source = fields.Float(required=True)
    consumption_ethanol_co2_stationary_source = fields.Float(required=True)
    consumption_ethanol_ch4_stationary_source = fields.Float(required=True)
    consumption_ethanol_n20_stationary_source = fields.Float(required=True)
    nitrogen_fertilization_green_fertilizer = fields.Float(required=True)
    land_occupation_1 = fields.Float(required=True)
    land_occupation_2 = fields.Float(required=True)
    land_occupation_3 = fields.Float(required=True)
    land_occupation_4 = fields.Float(required=True)
    land_occupation_5 = fields.Float(required=True)
    land_occupation_6 = fields.Float(required=True)
    land_occupation_7 = fields.Float(required=True)
    land_occupation_8 = fields.Float(required=True)
    land_occupation_9 = fields.Float(required=True)
    land_occupation_10 = fields.Float(required=True)
    land_occupation_11 = fields.Float(required=True)
    land_occupation_12 = fields.Float(required=True)
    land_occupation_13 = fields.Float(required=True)
    land_occupation_14 = fields.Float(required=True)
    land_occupation_15 = fields.Float(required=True)
    land_occupation_16 = fields.Float(required=True)
    land_occupation_17 = fields.Float(required=True)
    no_tillage_system_coverage = fields.Float(required=True)
    no_tillage_system = fields.Float(required=True)
    conventional_planting_system = fields.Float(required=True)


class CalculatorQuerySchema(Schema):
    owner_doc = fields.String(missing=None)

    @post_load
    def format(self, data: dict, **_):
        return {key: value for key, value in data.items() if value is not None}
