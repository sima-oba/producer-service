import statistics

from ..model.calculator_settings import CalculatorSettings
from ..model.calculator_data_collect import CalculatorDataCollect
from ..model.calculator_result import CalculatorResult


class CalculatorHelper:
    def __init__(
        self, settings: CalculatorSettings, data: CalculatorDataCollect
    ):
        self._settings = settings
        self._data = data

        # Soy activity
        self._n_synthetic_fertilizer = None
        self._urea = None
        self._n_organic_fertilizer = None
        self._direct_synthetic_fertilization = None
        self._synthetic_fertilization_with_volatilization = None
        self._synthetic_fertilization_with_leaching = None
        self._soil_correction_and_conditioning = None
        self._cultural_remains = None
        self._fuel_consumption = None
        self._organic_soil = None
        self._green_fertilization = None
        self._electricity_purchase = None
        self._average_production = None

        # Second crop activity
        self._n_synthetic_fertilizer_second_crop = None
        self._urea_second_crop = None
        self._n_organic_fertilizer_second_crop = None
        self._direct_synthetic_fertilization_second_crop = None
        self._synthetic_fertilization_with_volatilization_second_crop = None
        self._synthetic_fertilization_with_leaching_second_crop = None
        self._soil_correction_and_conditioning_second_crop = None
        self._cultural_remains_second_crop = None
        self._green_fertilization_second_crop = None

        # GEE emission
        self._gee_emission = None
        self._gee_emission_per_area = None
        self._gee_emission_per_bag = None

        self._baseline_emission = None
        self._baseline_removal = None
        self._baseline = None
        self._baseline_per_area = None
        self._baseline_per_bag = None

        # Sceneries
        self._scenery_1_removal = None
        self._scenery_2_removal = None
        self._scenery_3_removal = None
        self._scenery_4_removal = None
        self._gee_scenery_1 = None
        self._gee_scenery_2 = None
        self._gee_scenery_3 = None
        self._gee_scenery_4 = None
        self._gee_scenery_1_per_area = None
        self._gee_scenery_2_per_area = None
        self._gee_scenery_3_per_area = None
        self._gee_scenery_4_per_area = None
        self._gee_scenery_1_per_bag = None
        self._gee_scenery_2_per_bag = None
        self._gee_scenery_3_per_bag = None
        self._gee_scenery_4_per_bag = None

        self._baseline_c_stock = None
        self._rl_c_stock = None
        self._app_c_stock = None
        self._forest_c_stock = None
        self._emission_n_synthetic_fertilizer = None
        self._emission_urea = None
        self._emission_n_organic_fertilizer = None
        self._emission_leaching = None
        self._emission_volatilization = None
        self._emission_liming_and_plastering = None
        self._emission_waste_decomposition = None
        self._emission_organic_soils_handling = None
        self._emission_operations = None

        self._production_transport = None
        self._biogenic_fuel_consumption = None
        self._mechanized_and_stationary_operation = None
        self._non_mechanized_operation = None

    def calculate(self) -> CalculatorResult:
        self._calc_n_synthetic_fertilizer()
        self._calc_direct_synthetic_fertilization()
        self._calc_synthetic_fertilization_with_volatilization()
        self._calc_synthetic_fertilization_with_leaching()
        self._calc_soil_correction_and_conditioning()
        self._calc_cultural_remains()
        self._calc_green_fertilization()

        self._calc_n_synthetic_fertilizer_second_crop()
        self._calc_direct_synthetic_fertilization_second_crop()
        self._calc_synthetic_fertilization_with_volatilization_second_crop()
        self._calc_synthetic_fertilization_with_leaching_second_crop()
        self._calc_soil_correction_and_conditioning_second_crop()
        self._calc_cultural_remains_second_crop()
        self._calc_green_fertilization_second_crop()

        self._calc_fuel_consumption()
        self._calc_organic_soil()
        self._calc_electricity_purchase()
        self._calc_average_production()
        self._calc_gee_emission()
        self._calc_gee_emission_per_area()
        self._calc_gee_emission_per_bag()
        self._calc_baseline_emission()
        self._calc_baseline_removal()
        self._calc_baseline()
        self._calc_baseline_per_area()
        self._calc_baseline_per_bag()
        self._calc_sceneries()
        self._calc_baseline_c_stock()
        self._calc_emission_fertilizer_n_synthetic()
        self._calc_emission_urea()
        self._calc_emission_n_organic_fertilizer()
        self._calc_emission_leaching()
        self._calc_emission_volatilization()
        self._calc_emission_liming_and_plastering()
        self._calc_emission_waste_decomposition()
        self._calc_emission_organic_soils_handling()
        self._calc_mechanized_and_stationary_operation()
        self._calc_non_mechanized_operation()
        self._calc_production_transport()

        return CalculatorResult(
            self._baseline,
            self._baseline_per_area,
            self._baseline_per_bag,
            self._gee_scenery_1,
            self._gee_scenery_2,
            self._gee_scenery_3,
            self._gee_scenery_4,
            self._gee_scenery_1_per_area,
            self._gee_scenery_2_per_area,
            self._gee_scenery_3_per_area,
            self._gee_scenery_4_per_area,
            self._gee_scenery_1_per_bag,
            self._gee_scenery_2_per_bag,
            self._gee_scenery_3_per_bag,
            self._gee_scenery_4_per_bag,
            self._gee_emission,
            self._gee_emission_per_area,
            self._gee_emission_per_bag,
            self._baseline_emission,
            self._baseline_removal,
            self._scenery_1_removal,
            self._scenery_2_removal,
            self._scenery_3_removal,
            self._scenery_4_removal,
            self._baseline_c_stock,
            self._rl_c_stock,
            self._app_c_stock,
            self._forest_c_stock,
            self._emission_n_synthetic_fertilizer,
            self._emission_urea,
            self._emission_n_organic_fertilizer,
            self._emission_leaching,
            self._emission_volatilization,
            self._emission_liming_and_plastering,
            self._emission_waste_decomposition,
            self._emission_organic_soils_handling,
            self._fuel_consumption,
            self._electricity_purchase,
            self._production_transport,
            self._mechanized_and_stationary_operation,
            self._non_mechanized_operation,
        )

    def _calc_n_synthetic_fertilizer(self):
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg
                * self._data.synthetic_n_fertilizer_teor_type1
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg
                * self._data.synthetic_n_fertilizer_teor_type2
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg
                * self._data.synthetic_n_fertilizer_teor_type3
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._n_synthetic_fertilizer = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
        )

    def _calc_direct_synthetic_fertilization(self) -> float:
        # Adubação Nitrogenada (N) - DIRETA
        self._urea = (
            self._data.urea_type1 * self._settings.urea_co2
        ) / 1000 + (
            (self._data.urea_type1 * self._settings.urea_n2o)
            / 1000
            * self._settings.nitrous_oxide
        )
        self._n_organic_fertilizer = (
            (
                self._data.organic_n_fertilizer_type1_kg
                * self._settings.organic_n_fertilizer
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._direct_synthetic_fertilization = (
            self._n_synthetic_fertilizer
            + self._urea
            + self._n_organic_fertilizer
        )

    def _calc_synthetic_fertilization_with_volatilization(self):
        # Adubação Nitrogenada (N) - Volatilização/Dep. ATM
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg
                * self._data.synthetic_n_fertilizer_teor_type1
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg
                * self._data.synthetic_n_fertilizer_teor_type2
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg
                * self._data.synthetic_n_fertilizer_teor_type3
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        urea = (
            (
                self._data.urea_type1
                * self._settings.urea_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_organic_fertilizer = (
            (
                self._data.organic_n_fertilizer_type1_kg
                * self._settings.volatilization_n_residue
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._synthetic_fertilization_with_volatilization = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
            + urea
            + n_organic_fertilizer
        )

    def _calc_synthetic_fertilization_with_leaching(self):
        # Adubação Nitrogenada (N) - Lixiviação/Esc. Superficial
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg
                * self._data.synthetic_n_fertilizer_teor_type1
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg
                * self._data.synthetic_n_fertilizer_teor_type2
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg
                * self._data.synthetic_n_fertilizer_teor_type3
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        urea = (
            (
                self._data.urea_type1
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_organic_fertilizer = (
            (
                self._data.organic_n_fertilizer_type1_kg
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._synthetic_fertilization_with_leaching = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
            + urea
            + n_organic_fertilizer
        )

    def _calc_soil_correction_and_conditioning(self):
        # Correção e Condicionamento do solo
        calcitic_limestone = (
            self._data.calcitic_limestone * self._settings.calcitic_limestone
        ) / 1000
        dolomitic_limestone = (
            self._data.dolomitic_limestone * self._settings.dolomitic_limestone
        ) / 1000
        agricultural_plaster = (
            self._data.agricultural_plaster
            * self._settings.agricultural_plaster
        ) / 1000

        self._soil_correction_and_conditioning = (
            calcitic_limestone + dolomitic_limestone + agricultural_plaster
        )

    def _calc_cultural_remains(self):
        # Decomposição de Restos Culturais
        self._cultural_remains = (
            self._data.cultivated_area
            * (
                self._data.average_productivity
                * self._settings.soy_frac_dm
                / 1000
            )
            * self._settings.soy_slope
            * self._settings.soy_intercept
            * 1000
            * self._settings.soy_nag
            * (1 - self._data.waste_field)
            + (
                self._data.cultivated_area
                * (
                    (
                        self._data.average_productivity
                        * self._settings.soy_frac_dm
                        / 1000
                    )
                    * self._settings.soy_slope
                    * self._settings.soy_intercept
                    * 1000
                    + self._data.average_productivity
                    * self._settings.soy_frac_dm
                )
                * self._settings.soy_rbg_bio
                * self._settings.soy_nbg
            )
            * 0.01
            * (44 / 28)
            * self._settings.nitrous_oxide
        ) / 1000

    def _calc_green_fertilization(self):
        # Adubação Verde
        legume = (
            self._data.green_adubation
            * self._settings.green_fertilizer_1
            / 1000
            * self._settings.nitrous_oxide
        )
        grass = (
            self._data.grassy_type1_kg
            * self._settings.green_fertilizer_2
            / 1000
            * self._settings.nitrous_oxide
        )
        other = (
            self._data.others_type1_kg
            * self._settings.green_fertilizer_3
            / 1000
            * self._settings.nitrous_oxide
        )

        self._green_fertilization = legume + grass + other

    def _calc_n_synthetic_fertilizer_second_crop(self):
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type1_second_crop
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type2_second_crop
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type3_second_crop
                * self._settings.synthetic_fertilization
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._n_synthetic_fertilizer_second_crop = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
        )

    def _calc_direct_synthetic_fertilization_second_crop(self):
        # Adubação Nitrogenada (N) - DIRETA - 2 Safra
        self._urea_second_crop = (
            self._data.urea_type1_second_crop * self._settings.urea_co2
        ) / 1000 + (
            (self._data.urea_type1_second_crop * self._settings.urea_n2o)
            / 1000
            * self._settings.nitrous_oxide
        )
        self._n_organic_fertilizer_second_crop = (
            (
                self._data.organic_n_fertilizer_type1_kg_second_crop
                * self._settings.organic_n_fertilizer
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._direct_synthetic_fertilization_second_crop = (
            self._n_synthetic_fertilizer_second_crop
            + self._urea_second_crop
            + self._n_organic_fertilizer_second_crop
        )

    def _calc_synthetic_fertilization_with_volatilization_second_crop(self):
        # Adubação Nitrogenada (N) - Volatilização/Dep. ATM - 2 Safra
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type1_second_crop
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type2_second_crop
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type3_second_crop
                * self._settings.synthetic_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        urea = (
            (
                self._data.urea_type1_second_crop
                * self._settings.urea_n_volatilization
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_organic_fertilizer = (
            (
                self._data.organic_n_fertilizer_type1_kg_second_crop
                * self._settings.volatilization_n_residue
                * self._settings.atmospheric_deposition
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._synthetic_fertilization_with_volatilization_second_crop = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
            + urea
            + n_organic_fertilizer
        )

    def _calc_synthetic_fertilization_with_leaching_second_crop(self):
        # Adubação Nitrogenada (N) - Lixiviação/Esc. Superficial - 2 Safra
        n_synthetic_fertilizer_1 = (
            (
                self._data.synthetic_n_fertilizer_type1_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type1_second_crop
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_2 = (
            (
                self._data.synthetic_n_fertilizer_type2_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type2_second_crop
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_synthetic_fertilizer_3 = (
            (
                self._data.synthetic_n_fertilizer_type3_kg_second_crop
                * self._data.synthetic_n_fertilizer_teor_type3_second_crop
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        urea = (
            (
                self._data.urea_type1_second_crop
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )
        n_organic_fertilizer = (
            (
                self._data.organic_n_fertilizer_type1_kg_second_crop
                * self._settings.leaching
                * self._settings.leaching_n_fertilizer
                * (44 / 28)
            )
            / 1000
            * self._settings.nitrous_oxide
        )

        self._synthetic_fertilization_with_leaching_second_crop = (
            n_synthetic_fertilizer_1
            + n_synthetic_fertilizer_2
            + n_synthetic_fertilizer_3
            + urea
            + n_organic_fertilizer
        )

    def _calc_soil_correction_and_conditioning_second_crop(self):
        # Correção e Condicionamento do solo - 2 Safra
        calcitic_limestone = (
            self._data.calcitic_limestone_second_crop
            * self._settings.calcitic_limestone
        ) / 1000
        dolomitic_limestone = (
            self._data.dolomitic_limestone_second_crop
            * self._settings.dolomitic_limestone
        ) / 1000
        agricultural_plaster = (
            self._data.agricultural_plaster_second_crop
            * self._settings.agricultural_plaster
        ) / 1000

        self._soil_correction_and_conditioning_second_crop = (
            calcitic_limestone + dolomitic_limestone + agricultural_plaster
        )

    def _calc_cultural_remains_second_crop(self):
        # Decomposição de Restos Culturais - 2 Safra
        self._cultural_remains_second_crop = (
            self._data.cultivated_area_second_crop
            * (
                self._data.average_productivity_second_crop
                * self._settings.corn_frac_dm_second_crop
                / 1000
            )
            * self._settings.corn_slope_second_crop
            * self._settings.corn_intercept_second_crop
            * 1000
            * self._settings.corn_nag_second_crop
            * (1 - self._data.waste_field_second_crop)
            + (
                self._data.cultivated_area_second_crop
                * (
                    (
                        self._data.average_productivity_second_crop
                        * self._settings.corn_frac_dm_second_crop
                        / 1000
                    )
                    * self._settings.corn_slope_second_crop
                    * self._settings.corn_intercept_second_crop
                    * 1000
                    + self._data.average_productivity_second_crop
                    * self._settings.corn_frac_dm_second_crop
                )
                * self._settings.corn_rbg_bio_second_crop
                * self._settings.corn_nbg_second_crop
            )
            * 0.01
            * (44 / 28)
            * self._settings.nitrous_oxide
        ) / 1000

    def _calc_green_fertilization_second_crop(self):
        # Adubação Verde
        legume = (
            self._data.green_adubation_second_crop
            * self._settings.green_fertilizer_1
            / 1000
            * self._settings.nitrous_oxide
        )
        grass = (
            self._data.grassy_type1_kg_second_crop
            * self._settings.green_fertilizer_2
            / 1000
            * self._settings.nitrous_oxide
        )
        other = (
            self._data.others_type1_kg_second_crop
            * self._settings.green_fertilizer_3
            / 1000
            * self._settings.nitrous_oxide
        )

        self._green_fertilization_second_crop = legume + grass + other

    def _calc_fuel_consumption(self):
        # Consumo de Combustíveis
        gasoline_mechanized = (
            self._data.gasoline_mechanical_operation
            * self._settings.regular_gasoline
            * self._settings.consumption_gasoline
        )
        diesel_mechanized = (
            self._data.diesel_b10_mechanical_operation
            * self._settings.diesel_b10
            * self._settings.diesel_c02_mobile_source
            + (
                self._data.diesel_b10_mechanical_operation
                * self._settings.diesel_b10
                * self._settings.diesel_ch4_mobile_source
                * self._settings.methane
            )
            + (
                self._settings.diesel_n2o_mobile_source
                * self._settings.nitrous_oxide
            )
        ) / 1000
        gasoline_stationary = (
            self._data.gasoline_stationary_operation
            * self._settings.regular_gasoline
            * self._settings.consumption_gasoline
        )
        diesel_stationary = (
            self._data.diesel_b10_stationary_operation
            * self._settings.diesel_b10
            * self._settings.diesel_c02_stationary_source
            + self._data.diesel_b10_stationary_operation
            * self._settings.diesel_b10
            * self._settings.diesel_ch4_stationary_source
            * self._settings.methane
            + self._data.diesel_b10_stationary_operation
            * self._settings.diesel_b10
            * self._settings.diesel_n20_stationary_source
            * self._settings.nitrous_oxide
        ) / 1000

        self._fuel_consumption = (
            gasoline_mechanized
            + diesel_mechanized
            + gasoline_stationary
            + diesel_stationary
        )

    def _calc_organic_soil(self):
        # Solo Orgânico
        self._organic_soil = (
            self._data.area_organic_soils
            * self._settings.organic_soils_cultivation
            + self._data.area_organic_soils
            * self._settings.nitrogen_loss
            * self._settings.nitrous_oxide
        )

    def _calc_electricity_purchase(self):
        self._electricity_purchase = (
            self._data.energy_consumption
            * statistics.mean(
                [
                    self._settings.purchase_of_electricity_2019,
                    self._settings.purchase_of_electricity_2020,
                ]
            )
        )

    def _calc_average_production(self):
        self._average_production = (
            self._data.average_productivity * self._data.cultivated_area
        )

    def _calc_gee_emission(self):
        soy_activity = (
            self._direct_synthetic_fertilization
            + self._synthetic_fertilization_with_volatilization
            + self._synthetic_fertilization_with_leaching
            + self._soil_correction_and_conditioning
            + self._cultural_remains
            + self._fuel_consumption
            + self._organic_soil
            + self._green_fertilization
        )

        second_crop_activity = (
            self._direct_synthetic_fertilization_second_crop
            + self._synthetic_fertilization_with_volatilization_second_crop
            + self._synthetic_fertilization_with_leaching_second_crop
            + self._soil_correction_and_conditioning_second_crop
            + self._cultural_remains_second_crop
            + self._green_fertilization_second_crop
        )

        self._gee_emission = (
            soy_activity + second_crop_activity + self._electricity_purchase
        )

    def _calc_gee_emission_per_area(self):
        if self._data.cultivated_area > 0:
            self._gee_emission_per_area = (
                self._gee_emission / self._data.cultivated_area
            )
        else:
            self._gee_emission_per_area = 0

    def _calc_gee_emission_per_bag(self):
        if self._average_production > 0:
            self._gee_emission_per_bag = self._gee_emission / (
                self._average_production / 60
            )
        else:
            self._gee_emission_per_bag = 0

    def _calc_baseline_emission(self):
        self._baseline_emission = 0

        if self._data.cultivation_system > 0:
            self._baseline_emission = (
                self._data.cultivation_system * self._data.cultivated_area
            )

    def _calc_baseline_removal(self):
        self._baseline_removal = 0

        if self._baseline_emission == 0:
            self._baseline_removal = (
                (self._data.cultivated_area - self._data.coverage_use)
                * self._settings.no_tillage_system
                + self._data.coverage_use
                * self._settings.no_tillage_system_coverage
            )

    def _calc_baseline(self):
        self._baseline = (
            self._gee_emission +
            self._baseline_emission +
            self._baseline_removal
        )

    def _calc_baseline_per_area(self):
        if self._data.cultivated_area > 0:
            self._baseline_per_area = (
                self._baseline / self._data.cultivated_area
            )
        else:
            self._baseline_per_area = 0

    def _calc_baseline_per_bag(self):
        if self._average_production > 0:
            self._baseline_per_bag = self._baseline / (
                self._average_production / 60
            )
        else:
            self._baseline_per_bag = 0

    def _calc_sceneries(self):
        self._scenery_1_removal = (
            self._data.cultivated_area * self._settings.land_occupation_11
        )
        self._scenery_2_removal = (
            self._data.cultivated_area * self._settings.land_occupation_14
        )
        self._scenery_3_removal = (
            self._data.cultivated_area * self._settings.land_occupation_6
        )
        self._scenery_4_removal = (
            self._data.cultivated_area * self._settings.land_occupation_2
        )

        self._gee_scenery_1 = self._gee_emission + self._scenery_1_removal
        self._gee_scenery_2 = self._gee_emission + self._scenery_2_removal
        self._gee_scenery_3 = self._gee_emission + self._scenery_3_removal
        self._gee_scenery_4 = self._gee_emission + self._scenery_4_removal

        if self._data.cultivated_area > 0:
            self._gee_scenery_1_per_area = (
                self._gee_scenery_1 / self._data.cultivated_area
            )
            self._gee_scenery_2_per_area = (
                self._gee_scenery_2 / self._data.cultivated_area
            )
            self._gee_scenery_3_per_area = (
                self._gee_scenery_3 / self._data.cultivated_area
            )
            self._gee_scenery_4_per_area = (
                self._gee_scenery_4 / self._data.cultivated_area
            )
        else:
            self._gee_scenery_1_per_area = 0
            self._gee_scenery_2_per_area = 0
            self._gee_scenery_3_per_area = 0
            self._gee_scenery_4_per_area = 0

        if self._average_production > 0:
            self._gee_scenery_1_per_bag = self._gee_scenery_1 / (
                self._average_production / 60
            )
            self._gee_scenery_2_per_bag = self._gee_scenery_2 / (
                self._average_production / 60
            )
            self._gee_scenery_3_per_bag = self._gee_scenery_3 / (
                self._average_production / 60
            )
            self._gee_scenery_4_per_bag = self._gee_scenery_4 / (
                self._average_production / 60
            )
        else:
            self._gee_scenery_1_per_bag = 0
            self._gee_scenery_2_per_bag = 0
            self._gee_scenery_3_per_bag = 0
            self._gee_scenery_4_per_bag = 0

    def _calc_baseline_c_stock(self):
        if not self._data.biome_1_coverage:
            self._data.biome_1 = 0

        if not self._data.biome_2_coverage:
            self._data.biome_2 = 0

        if not self._data.biome_3_coverage:
            self._data.biome_3 = 0

        biomes_average = statistics.mean(
            [self._data.biome_1, self._data.biome_2, self._data.biome_3]
        )

        self._rl_c_stock = self._data.rl * biomes_average
        self._app_c_stock = self._data.app * biomes_average
        self._forest_c_stock = self._data.forest_surplus * biomes_average

        self._baseline_c_stock = (
            self._rl_c_stock + self._app_c_stock + self._forest_c_stock
        )

    def _calc_emission_fertilizer_n_synthetic(self):
        self._emission_n_synthetic_fertilizer = (
            self._n_synthetic_fertilizer
            + self._n_synthetic_fertilizer_second_crop
        )

    def _calc_emission_urea(self):
        self._emission_urea = self._urea + self._urea_second_crop

    def _calc_emission_n_organic_fertilizer(self):
        self._emission_n_organic_fertilizer = (
            self._n_organic_fertilizer + self._n_organic_fertilizer_second_crop
        )

    def _calc_emission_leaching(self):
        self._emission_leaching = (
            self._synthetic_fertilization_with_leaching
            + self._synthetic_fertilization_with_leaching_second_crop
        )

    def _calc_emission_volatilization(self):
        self._emission_volatilization = (
            self._synthetic_fertilization_with_volatilization
            + self._synthetic_fertilization_with_volatilization_second_crop
        )

    def _calc_emission_liming_and_plastering(self):
        self._emission_liming_and_plastering = (
            self._soil_correction_and_conditioning
            + self._soil_correction_and_conditioning_second_crop
        )

    def _calc_emission_waste_decomposition(self):
        self._emission_waste_decomposition = (
            self._cultural_remains + self._cultural_remains_second_crop
        )

    def _calc_emission_organic_soils_handling(self):
        self._emission_organic_soils_handling = (
            self._data.area_organic_soils
            * self._settings.organic_soils_cultivation
            + (
                self._data.area_organic_soils
                * self._settings.nitrogen_loss
                * self._settings.nitrous_oxide
            )
        )

    def _calc_mechanized_and_stationary_operation(self):
        biodiesel_mobile = (
            self._data.diesel_b10_mechanical_operation
            * (1 - self._settings.diesel_b10)
            * self._settings.consumption_biodiesel_co2_mobile_source
            + (
                self._data.diesel_b10_mechanical_operation
                * (1 - self._settings.diesel_b10)
                * self._settings.consumption_biodiesel_ch4_mobile_source
                * self._settings.methane
            )
            + (
                self._data.diesel_b10_mechanical_operation
                * (1 - self._settings.diesel_b10)
                * self._settings.consumption_biodiesel_n20_mobile_source
                * self._settings.nitrous_oxide
            )
        ) / 1000
        biodiesel_stationary = 0
        ethanol_mobile = 0
        ethanol_stationary = (
            (
                self._data.hydrous_ethanol_mechanical_operation
                + (
                    self._data.gasoline_stationary_operation
                    * (1 - self._settings.regular_gasoline)
                )
            )
            * self._settings.consumption_ethanol_co2_stationary_source
            + (
                self._data.hydrous_ethanol_mechanical_operation
                + (
                    self._data.gasoline_stationary_operation
                    * (1 - self._settings.regular_gasoline)
                )
            )
            * self._settings.consumption_ethanol_ch4_stationary_source
            * self._settings.methane
            + (
                self._data.hydrous_ethanol_mechanical_operation
                + (
                    self._data.gasoline_stationary_operation
                    * (1 - self._settings.regular_gasoline)
                )
            )
            * self._settings.consumption_ethanol_n20_stationary_source
            * self._settings.nitrous_oxide
        ) / 1000

        self._mechanized_and_stationary_operation = (
            biodiesel_mobile
            + biodiesel_stationary
            + ethanol_mobile
            + ethanol_stationary
        )

    def _calc_non_mechanized_operation(self):
        green_fertilization = (
            self._data.green_adubation
            + self._data.grassy_type1_kg
            + self._data.agricultural_plaster
        )

        if green_fertilization > 0:
            activity = self._data.cultivated_area
        else:
            activity = 0

        self._non_mechanized_operation = (
            activity * self._settings.nitrogen_fertilization_green_fertilizer
        )

    def _calc_production_transport(self):
        self._production_transport = (
            self._data.transport_production_diesel_b10
            * self._settings.diesel_c02_mobile_source
            + (
                self._data.transport_production_diesel_b10
                * self._settings.diesel_ch4_mobile_source
                * self._settings.methane
            )
            + (
                self._data.transport_production_diesel_b10
                * self._settings.diesel_n2o_mobile_source
                * self._settings.nitrous_oxide
            )
        )
