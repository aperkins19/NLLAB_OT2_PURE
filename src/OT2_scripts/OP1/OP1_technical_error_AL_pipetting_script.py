from opentrons import protocol_api
import json

# metadata
metadata = {
    "protocolName": "OP1 plating v1",
    "author": "Alex Perkins",

    "email": "a.j.p.perkins@sms.ed.ac.uk",
    "description": "First draft of script to plate out 3x PURE rxns",
    "apiLevel": "2.5",
}

# Add 35ul of lysate to a PCR tube to A1 in cold block
# Defining the aspiration height for 35ul of lysate  "lysate_aspirate_height_init" : 4.5,

# Add 90ul of substrates mix to B1
# Defining the aspiration height for 90ul of substrates: "substrates_aspirate_height_init" : 8.6,

## Substate calculator on Labstep

# Protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # 0. Reading in json setting files-----------------------------------------

    experiment_prefix = "OP1"

    # Defining the file paths of raspberry pi
    experiment_settings_dict_path = "/data/user_storage/"+ experiment_prefix + "/" + experiment_prefix + "_experiment_settings.json"
    labware_settings_dict_path = "/data/user_storage/"+ experiment_prefix + "/" + experiment_prefix + "_labware_settings.json"
    pipetting_settings_dict_path = "/data/user_storage/" + experiment_prefix + "/" + experiment_prefix + "_pipetting_settings.json"
    reagent_sources_dict_path = "/data/user_storage/" + experiment_prefix + "/" + experiment_prefix + "_reagent_sources.json"

    # Reading in json json_settings_file
    experiment_settings_dict = json.load(open(experiment_settings_dict_path, 'r'))
    protocol.comment("Experiment settings json file was read in")

    labware_settings_dict = json.load(open(labware_settings_dict_path, 'r'))
    protocol.comment("Labware settings json file was read in")

    pipetting_settings_dict = json.load(open(pipetting_settings_dict_path, 'r'))
    protocol.comment("Pipetting settings json file was read in")

    reagent_sources_dict = json.load(open(reagent_sources_dict_path, 'r'))
    protocol.comment("Reagent Sources json file was read in")

    # 1. Defining variables used in protocol-----------------------------------

    # Defining the booleans for the protocol. This controls which parts of
    # the protocol to run.
    protocol_dispense_lysate = True
    protocol_dispense_subsrates = True
    protocol_dispense_wax = True

    # labware

    # Defining the temperature module
    temperature_module = protocol.load_module(labware_settings_dict["temp_module"]["name"], labware_settings_dict["temp_module"]["deck_position"])


    # Defining the pcr plate ontop of the temperature module
    # https://www.bio-rad.com/en-uk/sku/hsp9601-hard-shell-96-well-pcr-plates-low-profile-thin-wall-skirted-white-clear?ID=hsp9601
    pcr_temp_plate = temperature_module.load_labware(
        labware_settings_dict["pcr_temp_plate"]["name"],
        label="Temperature-Controlled Tubes",
    )

    protocol.comment(str(labware_settings_dict["nunc_384"]["offsets"]["x"]))

    pcr_temp_plate.set_offset(x = labware_settings_dict["pcr_temp_plate"]["offsets"]["x"],
                              y = labware_settings_dict["pcr_temp_plate"]["offsets"]["y"],
                              z = labware_settings_dict["pcr_temp_plate"]["offsets"]["z"])

    # Defining the 384 nunc well plate
    nunc_384 = protocol.load_labware(labware_settings_dict["nunc_384"]["name"], labware_settings_dict["nunc_384"]["deck_position"])

    nunc_384.set_offset(x = labware_settings_dict["nunc_384"]["offsets"]["x"],
                                  y = labware_settings_dict["nunc_384"]["offsets"]["y"],
                                  z = labware_settings_dict["nunc_384"]["offsets"]["z"])


    # Defining the 1.5ul eppendorf rack
    eppendorf_1500ul_x24_rack = protocol.load_labware(
        labware_settings_dict["eppendorf_1500ul_x24_rack"]["name"], labware_settings_dict["eppendorf_1500ul_x24_rack"]["deck_position"]
    )

    eppendorf_1500ul_x24_rack.set_offset(x = labware_settings_dict["eppendorf_1500ul_x24_rack"]["offsets"]["x"],
                                  y = labware_settings_dict["eppendorf_1500ul_x24_rack"]["offsets"]["y"],
                                  z = labware_settings_dict["eppendorf_1500ul_x24_rack"]["offsets"]["z"])



    # Defining the 20ul tip rack
    tiprack_20ul = protocol.load_labware(labware_settings_dict["tiprack_20ul"]["name"], labware_settings_dict["tiprack_20ul"]["deck_position"])

    tiprack_20ul.set_offset(x = labware_settings_dict["tiprack_20ul"]["offsets"]["x"],
                                  y = labware_settings_dict["tiprack_20ul"]["offsets"]["y"],
                                  z = labware_settings_dict["tiprack_20ul"]["offsets"]["z"])


    # Defining left_pipette (p20)
    left_pipette = protocol.load_instrument(
        labware_settings_dict["left_pipette"]["name"], "left", tip_racks=[tiprack_20ul]
    )

    # Defining the 300ul tip rack
    tiprack_300ul = protocol.load_labware(labware_settings_dict["tiprack_300ul"]["name"], labware_settings_dict["tiprack_300ul"]["deck_position"])

    tiprack_300ul.set_offset(x = labware_settings_dict["tiprack_300ul"]["offsets"]["x"],
                                  y = labware_settings_dict["tiprack_300ul"]["offsets"]["y"],
                                  z = labware_settings_dict["tiprack_300ul"]["offsets"]["z"])


    # Defining right_pipette (p300)
    right_pipette = protocol.load_instrument(
        labware_settings_dict["right_pipette"]["name"], "right", tip_racks=[tiprack_300ul]
    )

    # 2. Defining functions used in this protocol------------------------------

    # distributing_components_to_master_mix_from_stock
    def distributing_components_to_master_mix_from_stock(well, components_source_well, lysate_aspirate_height):

        left_pipette.pick_up_tip()


        left_pipette.well_bottom_clearance.aspirate = lysate_aspirate_height
        left_pipette.well_bottom_clearance.dispense = pipetting_settings_dict["lysate_dispense_well_bottom_clearance"]

        # aspirate step
        left_pipette.aspirate(pipetting_settings_dict["lysate_aspirate_volume"], pcr_temp_plate[components_source_well], rate=pipetting_settings_dict["lysate_aspirate_rate"])
        left_pipette.move_to(pcr_temp_plate[components_source_well].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        left_pipette.move_to(pcr_temp_plate[components_source_well].top(10))

        # Dispense Step
        left_pipette.dispense(pipetting_settings_dict["lysate_dispense_volume"], pcr_temp_plate[well], rate=pipetting_settings_dict["lysate_dispense_rate"])
        left_pipette.touch_tip()

        left_pipette.move_to(pcr_temp_plate[well].top(10))

        left_pipette.drop_tip()


    # adding_and_mixing_ribosomes_with_components
    def adding_and_mixing_ribosomes_with_components(well, ribosomes_source_well, ribosome_aspirate_height):

        left_pipette.pick_up_tip()


        left_pipette.well_bottom_clearance.aspirate = ribosome_aspirate_height
        left_pipette.well_bottom_clearance.dispense = pipetting_settings_dict["lysate_dispense_well_bottom_clearance"]

        # aspirate step
        left_pipette.aspirate(pipetting_settings_dict["ribosomes_aspirate_volume"], pcr_temp_plate[ribosomes_source_well], rate=pipetting_settings_dict["ribosomes_aspirate_rate"])
        left_pipette.move_to(pcr_temp_plate[ribosomes_source_well].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        left_pipette.move_to(pcr_temp_plate[ribosomes_source_well].top(10))

        # Dispense Step
        left_pipette.dispense(pipetting_settings_dict["ribosomes_dispense_volume"], pcr_temp_plate[well], rate=pipetting_settings_dict["ribosomes_dispense_rate"])
        left_pipette.touch_tip()

        left_pipette.move_to(pcr_temp_plate[well].top(10))

        left_pipette.drop_tip()

    # Distributing lysate
    def distribute_lysate(well, source_well, lysate_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = lysate_aspirate_height
        left_pipette.well_bottom_clearance.dispense = pipetting_settings_dict["lysate_dispense_well_bottom_clearance"]

        # aspirate step
        left_pipette.aspirate(pipetting_settings_dict["lysate_aspirate_volume"], source_well, rate=pipetting_settings_dict["lysate_aspirate_rate"])
        left_pipette.move_to(source_well.top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(pipetting_settings_dict["lysate_dispense_volume"], nunc_384[well], rate=pipetting_settings_dict["lysate_dispense_rate"])
        left_pipette.touch_tip()

        left_pipette.drop_tip()

    # Distributing master mix Energy Solution, Buffer A, DNA, chi6, water etc.
    def distribute_substrates(well, source_well, substrates_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = substrates_aspirate_height
        left_pipette.well_bottom_clearance.dispense = pipetting_settings_dict["substrates_dispense_well_bottom_clearance"]

        # aspirate step
        left_pipette.aspirate(pipetting_settings_dict["substrates_aspirate_volume"], source_well, rate=pipetting_settings_dict["substrates_aspirate_rate"])
        left_pipette.move_to(source_well.top(-2))
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(pipetting_settings_dict["substrates_dispense_volume"], nunc_384[well], rate=pipetting_settings_dict["substrates_dispense_rate"])

        left_pipette.drop_tip()


    def dispense_wax_to_individual_replicate_set(dispense_well_list):

        """ defines the dispense wax function """

        # Pick up a 300ul tip
        #right_pipette.pick_up_tip()

        # Distributing 35ul of wax ontop of each well in dispense_well_list
        right_pipette.distribute(
            pipetting_settings_dict["wax_dispense_volume"],
            wax_source_well,
            [
                nunc_384.wells_by_name()[well_name].top(pipetting_settings_dict["wax_dispense_height"])
                for well_name in dispense_well_list
            ],
            new_tip = pipetting_settings_dict["wax_new_tip"],
            touch_tip = pipetting_settings_dict["wax_touch_tip"],
            air_gap = pipetting_settings_dict["wax_air_gap"],
            disposal_volume = pipetting_settings_dict["wax_disposal_volume"],
        )

        # Drops tip
        #right_pipette.drop_tip()


    # 3. Running protocol------------------------------------------------------




    # Set temperature of temperature module to 4 degrees. The protocol will pause
    # until this is reached.
    #temperature_module.set_temperature(4)

    # Extracting the different experiments from the experiments

    # settings file
    experiment_ids = experiment_settings_dict.keys()

    # Master Mix Compilation
    protocol.comment("Beginning Master Mix Compilations...")


    # Components distribution

    # toggle for components distribution
    components_distribution_step_toggle = True

    if components_distribution_step_toggle:

        protocol.comment("Distributing components from stock to master mix wells...")

        #initialise ribosome_aspirate_height
        lysate_aspirate_height = pipetting_settings_dict["lysate_aspirate_height_init"]

        # loop over the experiments settings dict to get the lysate source wells
        # which are the component master mixes for each experiment
        for exp in experiment_settings_dict:

            # set the master mix well
            components_master_mix_well = experiment_settings_dict[exp]["lysate_source_well"]

            # look up where the master stock of components are
            components_source_well = reagent_sources_dict["Components"]["Base_System"]["Well"]

            protocol.comment(components_source_well)

            distributing_components_to_master_mix_from_stock(components_master_mix_well, components_source_well, lysate_aspirate_height)


        protocol.comment("Distributing components complete.")




    # Ribosome Addition

    # toggle for ribosome adding_and_mixing_ribosomes_with_components
    ribosome_mixing_step_toggle = True

    if ribosome_mixing_step_toggle:

        protocol.comment("Adding and mixing ribosomes with components...")

        #initialise ribosome_aspirate_height
        ribosome_aspirate_height = pipetting_settings_dict["ribosomes_aspirate_height_init"]

        # loop over the experiments settings dict to get the lysate source wells
        # which are the component master mixes for each experiment
        for exp in experiment_settings_dict:

            # set the master mix well
            components_master_mix_well = experiment_settings_dict[exp]["lysate_source_well"]

            # look up where the master stock of ribosomes are
            ribosomes_source_well = reagent_sources_dict["Components"]["Supplimentry_Components"]["Ribosomes"]["Well"]

            protocol.comment(ribosomes_source_well)

            adding_and_mixing_ribosomes_with_components(components_master_mix_well, ribosomes_source_well, ribosome_aspirate_height)


        protocol.comment("Ribosome mix step complete.")



    protocol.comment(" ")
    protocol.comment("Master Mix compliations complete.")

    # Running the substrate dispense step if protocol_dispense_subsrates = True
    if protocol_dispense_subsrates:

        protocol.comment("Beginning substrates plating step...")

        # Looping through the different experiments
        for experiment_id in experiment_ids:

            # Defining the source well for the substrates master mix
            substrates_source_well = pcr_temp_plate[experiment_settings_dict[experiment_id]["substrates_source_well"]]

            # Defining a list of wells for dispensing
            dispense_well_list = experiment_settings_dict[experiment_id]["dispense_well_list"]

            # Defining the initial lysate aspiration height
            substrates_aspirate_height = pipetting_settings_dict["substrates_aspirate_height_init"]

            # Dispensing substrates into each of the wells in dispense well list
            for well in dispense_well_list:

                # Caliing function to distribute substrates
                distribute_substrates(
                    well, substrates_source_well, substrates_aspirate_height
                )

                # Reducing the aspiration height by subsrates_aspirate_height_inc
                substrates_aspirate_height -= pipetting_settings_dict["substrates_aspirate_height_inc"]


            protocol.comment("Substrate dispense step complete for experiment " + experiment_id)




    # Running the lysate dispense step if protocol_dispense_lysate = True
    if protocol_dispense_lysate:

        # Looping through the different experiments
        for experiment_id in experiment_ids:

            # Outputting the name of the experiment that is being ran
            protocol.comment("Running experiment " + experiment_id)

            # Defining the source wells for the different components in this experiment
            lysate_source_well = pcr_temp_plate[experiment_settings_dict[experiment_id]["lysate_source_well"]]

            # Defining a list of wells for dispensing
            dispense_well_list = experiment_settings_dict[experiment_id]["dispense_well_list"]

            # Defining the initial lysate aspiration height
            lysate_aspirate_height = pipetting_settings_dict["lysate_aspirate_height_init"]

            # Dispensing lysate into each of the wells in dispense well list
            for well in dispense_well_list:

                # Caliing function to distribute lysate
                distribute_lysate(well, lysate_source_well, lysate_aspirate_height)

                # Reducing the aspiration height by lysate_aspirate_height_inc
                lysate_aspirate_height -= pipetting_settings_dict["lysate_aspirate_height_inc"]

            protocol.comment("Lysate dispense step complete for experiment " + experiment_id)



    # Pausing protocol so the plate can be span down in the centrifuge before

    # Turning off temp module after all experiments have finished
    temperature_module.deactivate()

    # adding the wax ontop
    protocol.pause("Check plate and spin down, before replacing for wax")


    # Running the wax dispense step if protocol_dispense_wax = True
    if protocol_dispense_wax:

        # Looping through the different experiments
        for experiment_id in experiment_ids:

            # Defining a list of wells for dispensing
            dispense_well_list = experiment_settings_dict[experiment_id]["dispense_well_list"]

            # Defining the source well for the wax
            wax_source_well = eppendorf_1500ul_x24_rack.wells_by_name()[experiment_settings_dict[experiment_id]["wax_source_well"]]

            dispense_wax_to_individual_replicate_set(dispense_well_list)

            protocol.comment("Wax dispense step complete for experiment " + experiment_id)
