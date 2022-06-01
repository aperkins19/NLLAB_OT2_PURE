from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Lysate CFPS Plating Script v1',
    'author': 'Alex Perkins',
    'email': 'a.j.p.perkins@sms.ed.ac.uk',
    'description': 'First draft of script to plate out 10x lysate reactions',
    'apiLevel': '2.3'
}

# Add 35ul of lysate to a PCR tube to A1 in cold block
# Add 90ul of substrates mix to B1
#dispense_well_list = ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']



# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware

    # temperature module
    temperature_module = protocol.load_module('temperature module gen2', 10)
    pcr_temp_plate = temperature_module.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul',
                                      label='Temperature-Controlled Tubes')


    nunc_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', '7')

    #eppendorf_1500ul_x24_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '8')

    # Defining left_pipette pipette and tip rack
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_20ul])

    # Defining p300 pipette and tip rack
    #tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '6')
    #p300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack_300ul])

    #    commands
    ## Set temperature
    temperature_module.set_temperature(4)



    dispense_well_list = ['B12','B13','B14','B15','B16','B17','B18','B19','B20','B21']

    ############################################################################################################################

    # first laydown the lysate
    def distribute_lysate(well, lysate_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = lysate_aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.1

        # aspirate step
        left_pipette.aspirate(3, pcr_temp_plate['A1'], rate=0.2)
        left_pipette.move_to(pcr_temp_plate['A1'].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(2.5, nunc_384[well], rate=0.1)
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        left_pipette.drop_tip()

    # exactly 5.2mm is 30ul of lysate in pcr
    lysate_aspirate_height = 4.5

    dispense_well_list = dispense_well_list

    for well in dispense_well_list:
        distribute_lysate(well, lysate_aspirate_height)
        lysate_aspirate_height -= 0.4


    ##################################################################################################################

    # Next, Distribute the Energy Solution, water, DNA Mix
    def distribute_substrates(well, substrates_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = substrates_aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.2

        # aspirate step
        left_pipette.aspirate(8, pcr_temp_plate['B1'], rate=1)
        left_pipette.move_to(pcr_temp_plate['B1'].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(7.5, nunc_384[well], rate=1)
        protocol.delay(seconds=2)

        left_pipette.touch_tip()

        left_pipette.drop_tip()


    # exactly 5.2mm is 30ul of lysate in pcr
    substrates_aspirate_height = 9

    dispense_well_list = dispense_well_list

    for well in dispense_well_list:
        distribute_substrates(well, substrates_aspirate_height)
        substrates_aspirate_height -= 0.8

    ####################################################################################################

    #protocol.pause('Check plate and spin down, before replacing for wax')

    ########################################################################################################

    # last laydown the wax

    #p300.pick_up_tip()

    #p300.distribute(35,
    #        eppendorf_1500ul_x24_rack.wells_by_name()['A1'],
    #        [nunc_384.wells_by_name()[well_name].top(5) for well_name in dispense_well_list],
    #        new_tip='never',
    #        touch_tip=True,
    #        air_gap=20,
    #        disposal_volume=30,
    #        )

    #p300.drop_tip()

    ## exactly 5.2mm is 30ul of lysate in pcr
    #lysate_aspirate_height = 4.5

    #dispense_well_list = dispense_well_list

    #for well in dispense_well_list:
        #pass

        #distribute_lysate(well, lysate_aspirate_height)
    #    lysate_aspirate_height -= 0.4



    # turn off temp module
    temperature_module.deactivate()
