from dataclasses import dataclass


@dataclass
class CalculatorResult:
    baseline: float
    baseline_per_area: float
    baseline_per_bag: float
    gee_scenery_1: float
    gee_scenery_2: float
    gee_scenery_3: float
    gee_scenery_4: float
    gee_scenery_1_per_area: float
    gee_scenery_2_per_area: float
    gee_scenery_3_per_area: float
    gee_scenery_4_per_area: float
    gee_scenery_1_per_bag: float
    gee_scenery_2_per_bag: float
    gee_scenery_3_per_bag: float
    gee_scenery_4_per_bag: float

    gee_emission: float
    gee_emission_per_area: float
    gee_emission_per_bag: float

    baseline_emission: float
    baseline_removal: float
    scenery_1_removal: float
    scenery_2_removal: float
    scenery_3_removal: float
    scenery_4_removal: float

    baseline_c_stock: float
    rl_c_stock: float
    app_c_stock: float
    forest_c_stock: float
    emission_n_synthetic_fertilizer: float
    emission_urea: float
    emission_n_organic_fertilizer: float
    emission_leaching: float
    emission_volatilization: float
    emission_liming_and_plastering: float
    emission_waste_decomposition: float
    emission_organic_soils_handling: float
    fuel_consumption: float

    electricity_purchase: float
    production_transport: float
    mechanized_and_stationary_operation: float
    non_mechanized_operation: float

    def __str__(self) -> str:
        return f'''
            Indicadores de Intensidade (Balanço de GEE)
            -------------------------------------------
            baseline:               {self.baseline}
            baseline_per_area:      {self.baseline_per_area}
            baseline_per_bag:       {self.baseline_per_bag}
            gee_scenery_1:          {self.gee_scenery_1}
            gee_scenery_2:          {self.gee_scenery_2}
            gee_scenery_3:          {self.gee_scenery_3}
            gee_scenery_4:          {self.gee_scenery_4}
            gee_scenery_1_per_area: {self.gee_scenery_1_per_area}
            gee_scenery_2_per_area: {self.gee_scenery_2_per_area}
            gee_scenery_3_per_area: {self.gee_scenery_3_per_area}
            gee_scenery_4_per_area: {self.gee_scenery_4_per_area}
            gee_scenery_1_per_bag:  {self.gee_scenery_1_per_bag}
            gee_scenery_2_per_bag:  {self.gee_scenery_2_per_bag}
            gee_scenery_3_per_bag:  {self.gee_scenery_3_per_bag}
            gee_scenery_4_per_bag:  {self.gee_scenery_4_per_bag}

            Emissões de GEE
            -------------------------------------------
            gee_emission:           {self.gee_emission}
            gee_emission_per_area:  {self.gee_emission_per_area}
            gee_emission_per_bag:   {self.gee_emission_per_bag}

            Remoções de GEE
            -------------------------------------------
            baseline_emission:      {self.baseline_emission}
            baseline_removal:       {self.baseline_removal}
            scenery_1_removal:      {self.scenery_1_removal}
            scenery_2_removal:      {self.scenery_2_removal}
            scenery_3_removal:      {self.scenery_3_removal}
            scenery_4_removal:      {self.scenery_4_removal}

            Emissões Escopo 1
            -------------------------------------------
            baseline_c_stock:       {self.baseline_c_stock}
            rl_c_stock:             {self.rl_c_stock}
            app_c_stock:            {self.app_c_stock}
            forest_c_stock:         {self.forest_c_stock}
            n_synthetic_fertilizer: {self.emission_n_synthetic_fertilizer}
            urea:                   {self.emission_urea}
            n_organic_fertilizer:   {self.emission_n_organic_fertilizer}
            leaching:               {self.emission_leaching}
            volatilization:         {self.emission_volatilization}
            liming_and_plastering:  {self.emission_liming_and_plastering}
            waste_decomposition:    {self.emission_waste_decomposition}
            organic_soils_handling: {self.emission_organic_soils_handling}
            operations:             {self.fuel_consumption}

            Emissões Escopo 2
            -------------------------------------------
            electricity_purchase:   {self.electricity_purchase}

            Emissões Escopo 3
            -------------------------------------------
            production_transport:   {self.production_transport}

            Emissões Biogênicas
            -------------------------------------------
            mechanic_operation:     {self.mechanized_and_stationary_operation}
            non_mechanic_operation: {self.non_mechanized_operation}
        '''
