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




# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware

    # temperature module
    temperature_module = protocol.load_module('temperature module gen2', 10)
    pcr_temp_plate = temperature_module.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul',
                                      label='Temperature-Controlled Tubes')


    nunc_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', '7')

    # pipettes
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    left_pipette = protocol.load_instrument(
         'p20_single_gen2', 'left', tip_racks=[tiprack_20ul])

    #    commands
    ## Set temperature
    temperature_module.set_temperature(4)

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

    dispense_well_list = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10']

    for well in dispense_well_list:

        distribute_lysate(well, lysate_aspirate_height)
        lysate_aspirate_height -= 0.4


    ##################################################################################################################

    # Next, Distribute the Energy Solution, water, DNA Mix
    def distribute_substrates(well, substrates_aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = substrates_aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.1

        # aspirate step
        left_pipette.aspirate(8, pcr_temp_plate['B1'], rate=0.2)
        left_pipette.move_to(pcr_temp_plate['B1'].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(7.5, nunc_384[well], rate=0.1)
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        left_pipette.drop_tip()

    #################################################################################################


    # exactly 5.2mm is 30ul of lysate in pcr
    substrates_aspirate_height = 4.5

    dispense_well_list = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10']

    for well in dispense_well_list:

        distribute_substrates(well, substrates_aspirate_height)
        substrates_aspirate_height -= 0.4



    # turn off temp module
    temperature_module.deactivate()
