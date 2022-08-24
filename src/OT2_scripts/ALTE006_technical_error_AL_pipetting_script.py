from opentrons import protocol_api

# metadata
metadata = {
    "protocolName": "Lysate CFPS Plating Script v1",
    "author": "Alex Perkins",
    "email": "a.j.p.perkins@sms.ed.ac.uk",
    "description": "First draft of script to plate out 10x lysate reactions",
    "apiLevel": "2.3",
}

# Add 35ul of lysate to a PCR tube to A1 in cold block
# Add 90ul of substrates mix to B1
# dispense_well_list = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']

## substate calculator on Labstep

# Protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # 0. Defining variables used in protocol-----------------------------------

    # labware

    # Defining the temperature module
    temperature_module = protocol.load_module("temperature module gen2", 10)

    # Defining the pcr plate ontop of the temperature module
    pcr_temp_plate = temperature_module.load_labware(
        "opentrons_96_aluminumblock_generic_pcr_strip_200ul",
        label="Temperature-Controlled Tubes",
    )
    # Defining the 384 nunc well plate
    nunc_384 = protocol.load_labware("corning_384_wellplate_112ul_flat", "7")

    # Defining the 1.5ul eppendorf rack
    eppendorf_1500ul_x24_rack = protocol.load_labware(
        "opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", "8"
    )

    # Defining the 20ul tip rack
    tiprack_20ul = protocol.load_labware("opentrons_96_tiprack_20ul", "9")

    # Defining left_pipette (p20)
    left_pipette = protocol.load_instrument(
        "p20_single_gen2", "left", tip_racks=[tiprack_20ul]
    )

    # Defining the 300ul tip rack
    tiprack_300ul = protocol.load_labware("opentrons_96_tiprack_300ul", "6")

    # Defining right_pipette (p300)
    right_pipette = protocol.load_instrument(
        "p300_single_gen2", "right", tip_racks=[tiprack_300ul]
    )

    # Defining the eppendorf well where the wax is placed
    wax_source_well = eppendorf_1500ul_x24_rack.wells_by_name()["A1"]

    # defining where the regents are sourced from.
    MS_lysate_source_well = pcr_temp_plate["A1"]
    MS_substrates_source_well = pcr_temp_plate["B1"]

    AP_lysate_source_well = pcr_temp_plate["A2"]
    AP_substrates_source_well = pcr_temp_plate["B2"]


    # Defining the wells to dispense into
    AP_dispense_well_list = [
        "B3",
        "B5",
        "B7",
        "B9",
        "B11",
        "B13",
        "B15",
        "B17",
        "B19",
        "B21",
    ]

    # Defining the wells to dispense into
    MS_dispense_well_list = [
        "D3",
        "D5",
        "D7",
        "D9",
        "D11",
        "D13",
        "D15",
        "D17",
        "D19",
        "D21",
    ]


    # Opentron parameters

    OT2_Liquid_Handling_Parameter_Dict = {


    # Defining the aspiration height for 35ul of lysate
    "lysate_aspirate_height_init" : 4.5,

    # Defining the increment to move down the lysate aspiration height after
    # each aspiration
    "lysate_aspirate_height_inc" : 0.4,

    # Defining the aspiration height for 90ul of substrates
    "substrates_aspirate_height_init" : 8.6,

    # Defining the increment to move down the substrate aspiration height after
    # each aspiration
    "substrates_aspirate_height_inc" : 0.6,

    # Defining the dispense volume for wax
    "wax_dispense_volume" : 35,

    # Defining the dispense height above well for wax
    "wax_dispense_height" : -3,

    # Defining whether to get a new tip when distribting wax
    "wax_new_tip" : "never",

    # Defining whether to touch tip when distribting wax
    "wax_touch_tip" : False,

    # Defining air gap when distributing wax
    "wax_air_gap" : 20,

    # Defining the disposal volume that will be thrown away after distributing
    # wax
    "wax_disposal_volume" : 30

    }



    # # Defining the wells to dispense into
    # AP_dispense_well_list = ['G3','G5','G7','G9','G11','G13','G15','G17','G19','G21']

    protocol_dispense_lysate = True
    protocol_dispense_subsrates = True
    protocol_dispense_wax = True

    # 1. Defining functions used in this protocol------------------------------

    # Distributing lysate
    def distribute_lysate(well, source_well, lysate_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = lysate_aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.1

        # aspirate step
        left_pipette.aspirate(3, source_well, rate=0.2)
        left_pipette.move_to(source_well.top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(2.5, nunc_384[well], rate=0.1)
        left_pipette.touch_tip()

        left_pipette.drop_tip()

    # Distributing master mix Energy Solution, Buffer A, DNA, chi6, water etc.
    def distribute_substrates(well, source_well, substrates_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = substrates_aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.2

        # aspirate step
        left_pipette.aspirate(8, source_well, rate=1)
        left_pipette.move_to(source_well.top(-2))
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(7.5, nunc_384[well], rate=1)

        left_pipette.drop_tip()

    # 2. Running protocol------------------------------------------------------

    # Set temperature of temperature module to 4 degrees. The protocol will pause
    # until this is reached.
    temperature_module.set_temperature(4)




    ## First Set of Experiments

    ############################################################## AP -  lysate and then substrates

    if protocol_dispense_lysate:

        # Lysate then Substrates - AP
        ###
        # assigning the dispense well list for this run
        dispense_well_list = AP_dispense_well_list
        lysate_source_well = AP_lysate_source_well

        # init aspirating params
        lysate_aspirate_height = OT2_Liquid_Handling_Parameter_Dict["lysate_aspirate_height_init"]

        # Dispensing lysate into each of the dispense wells in dispense well list
        for well in dispense_well_list:

            # Caliing function to distribute lysate
            distribute_lysate(well, lysate_source_well, lysate_aspirate_height)

            # Reducing the aspiration height by lysate_aspirate_height_inc
            lysate_aspirate_height -= OT2_Liquid_Handling_Parameter_Dict["lysate_aspirate_height_inc"]


    if protocol_dispense_subsrates:
        # Dispensing subsrates master mix into each of the dispense wells in

        # assigning the dispense well list for this run
        dispense_well_list = AP_dispense_well_list
        substrates_source_well = AP_substrates_source_well

        substrates_aspirate_height = OT2_Liquid_Handling_Parameter_Dict["substrates_aspirate_height_init"]

        # dispense well list
        for well in dispense_well_list:

            # Caliing function to distribute substrates
            distribute_substrates(
                well, substrates_source_well, substrates_aspirate_height
            )

            # Reducing the aspiration height by subsrates_aspirate_height_inc
            substrates_aspirate_height -= OT2_Liquid_Handling_Parameter_Dict["substrates_aspirate_height_inc"]





    ############################################################## MS -  Substrates and then lysate

    if protocol_dispense_subsrates:
        # Dispensing subsrates master mix into each of the dispense wells in

        # assigning the dispense well list for this run
        dispense_well_list = MS_dispense_well_list
        substrates_source_well = MS_substrates_source_well

        substrates_aspirate_height = OT2_Liquid_Handling_Parameter_Dict["substrates_aspirate_height_init"]

        # dispense well list
        for well in dispense_well_list:

            # Caliing function to distribute substrates
            distribute_substrates(
                well, substrates_source_well, substrates_aspirate_height
            )

            # Reducing the aspiration height by subsrates_aspirate_height_inc
            substrates_aspirate_height -= OT2_Liquid_Handling_Parameter_Dict["substrates_aspirate_height_inc"]


    if protocol_dispense_lysate:

        ###
        # assigning the dispense well list for this run
        dispense_well_list = MS_dispense_well_list
        lysate_source_well = MS_lysate_source_well

        # init aspirating params
        lysate_aspirate_height = OT2_Liquid_Handling_Parameter_Dict["lysate_aspirate_height_init"]

        # Dispensing lysate into each of the dispense wells in dispense well list
        for well in dispense_well_list:

            # Caliing function to distribute lysate
            distribute_lysate(well, lysate_source_well, lysate_aspirate_height)

            # Reducing the aspiration height by lysate_aspirate_height_inc
            lysate_aspirate_height -= OT2_Liquid_Handling_Parameter_Dict["lysate_aspirate_height_inc"]



    ##########################################################################################################################################

    # wax

    #########################################################################################################################################

    # Pausing protocol so thr plate can be span down in the centrifuge before
    # adding the wax ontop
    protocol.pause("Check plate and spin down, before replacing for wax")


    def dispense_wax_to_individual_replicate_set(dispense_well_list):

        """ defines the dispense wax function """

        # Pick up a 300ul tip
        right_pipette.pick_up_tip()

        # Distributing 35ul of wax ontop of each well in dispense_well_list
        right_pipette.distribute(
            OT2_Liquid_Handling_Parameter_Dict["wax_dispense_volume"],
            wax_source_well,
            [
                nunc_384.wells_by_name()[well_name].top(OT2_Liquid_Handling_Parameter_Dict["wax_dispense_height"])
                for well_name in dispense_well_list
            ],
            new_tip = OT2_Liquid_Handling_Parameter_Dict["wax_new_tip"],
            touch_tip = OT2_Liquid_Handling_Parameter_Dict["wax_touch_tip"],
            air_gap = OT2_Liquid_Handling_Parameter_Dict["wax_air_gap"],
            disposal_volume = OT2_Liquid_Handling_Parameter_Dict["wax_disposal_volume"],
        )

        # Drops tip
        right_pipette.drop_tip()

    if protocol_dispense_wax:

        dispense_wax_to_individual_replicate_set(AP_dispense_well_list)

        dispense_wax_to_individual_replicate_set(MS_dispense_well_list)



    # Turning off temp module
    temperature_module.deactivate()
