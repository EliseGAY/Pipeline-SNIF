from snif import * #To launch the script : python3 snif.py
for c in [3,4,5]: #Number of components authorized. Here we don't fix the time periods : we let snif estimate it
        for w in [1,0.75,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.1]: #Iteration over values of the distance parameter w (high : better fit on recent times; low : better fit on ancient times)

            h_inference_parameters = InferenceParameters(
        data_source = 'psmc_results/XX.psmc', #In a directory with psmc outputs, select one
        source_type = SourceType.PSMC,
        IICR_type = IICRType.Exact,
        ms_reference_size = 5000,
        ms_simulations = int(1e5),
        psmc_mutation_rate = 1.93e-8, #Change mutation rate
        psmc_number_of_sequences = 10,
        psmc_length_of_sequences = int(2e6),
        infer_scale = True,
        data_cutoff_bounds = (1e2, 2e5/11), #Period of psmc to fit
        data_time_intervals = 64,
        distance_function = ErrorFunction.ApproximatePDF,
        distance_parameter = w, #distance parameter
        distance_max_allowed = 7e3,
        distance_computation_interval = (3e2,1.5e5/11), #Must be within the bounds of "data_cutoff_bounds"
        rounds_per_test_bounds = (1, 3), 
        repetitions_per_test = 1,
        number_of_components = c, #number of components
        bounds_islands = (2, 100), #bounds for the number of demes
        bounds_migrations_rates = (0.05, 5000), #bounds for the connectivity rates
        bounds_deme_sizes = (1,1), #bounds for the deme size : don't change !
        bounds_event_times = (3e2, 1.5e5/11), #bounds to estimate the time of components (i.e when connectivity rate can change)
        bounds_effective_size = (100, 50000) #bounds for population size
)

            h_settings = Settings(
                static_library_location = './libs/libsnif.so',
                custom_filename_tag = 'Shark', #Tag for the outputs
                output_directory = './results/GN17525_50X_7kya_notfixed', #Name of output directory
                default_output_dirname = '_SNIF_results'
            )

            infer(inf = h_inference_parameters, settings = h_settings)