from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'General Liquid Characterisation Script',
    'author': 'Alex Perkins',
    'email': 'a.j.p.perkins@sms.ed.ac.uk',
    'description': 'Script to charcterise the pipetting error with handling different liquids.',
    'apiLevel': '2.3'
}


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware

    # temperature module
    temperature_module = protocol.load_module('temperature module gen2', 10)
    pcr_temp_plate = temperature_module.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul',
                                      label='Temperature-Controlled Tubes')

    # pipettes
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    left_pipette = protocol.load_instrument(
         'p20_single_gen2', 'left', tip_racks=[tiprack_20ul])

    #    commands

    # Dilutions
    """
    # first laydown the stock-30
    def distribute_stock_30(well, aspirate_height):

        right_pipette.pick_up_tip()

        right_pipette.well_bottom_clearance.aspirate = aspirate_height
        right_pipette.well_bottom_clearance.dispense = 7

        right_pipette.aspirate(100, reagent_falcon_block['A1'], rate=0.2)
        right_pipette.move_to(reagent_falcon_block['A1'].top(-2))
        protocol.delay(seconds=2)
        right_pipette.touch_tip()

        # Still dispensing 1mm above the bottom
        right_pipette.dispense(80, reagent_2ml_eppendorfs[well], rate=0.1)
        protocol.delay(seconds=2)
        right_pipette.touch_tip()

        right_pipette.blow_out(reagent_falcon_block['C1'])

        right_pipette.drop_tip()


    def distribute_bradford_reagent(well, aspirate_height):

        right_pipette.pick_up_tip()

        right_pipette.well_bottom_clearance.aspirate = aspirate_height
        right_pipette.well_bottom_clearance.dispense = 7

        right_pipette.aspirate(300, reagent_falcon_block['A1'], rate=0.5)
        right_pipette.move_to(reagent_falcon_block['A1'].top(-2))
        protocol.delay(seconds=2)
        right_pipette.touch_tip(reagent_2ml_eppendorfs['B1'])

        # Still dispensing 1mm above the bottom
        right_pipette.dispense(300, reagent_2ml_eppendorfs[well].bottom(10), rate=0.2)
        right_pipette.move_to(reagent_2ml_eppendorfs[well].top(3))
        right_pipette.blow_out()

        right_pipette.drop_tip()



    """
    # first laydown the lysate
    def distribute_lysate(well, aspirate_height):

        left_pipette.pick_up_tip()

        left_pipette.well_bottom_clearance.aspirate = aspirate_height
        left_pipette.well_bottom_clearance.dispense = 0.5

        # aspirate step
        left_pipette.aspirate(3, pcr_temp_plate['B10'], rate=0.2)
        left_pipette.move_to(pcr_temp_plate['B10'].top(-2))
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        # Dispense Step
        left_pipette.dispense(2.5, pcr_temp_plate[well], rate=0.1)
        protocol.delay(seconds=2)
        left_pipette.touch_tip()

        #right_pipette.blow_out(reagent_falcon_block['C1'])

        left_pipette.drop_tip()




    #################################################################################################
    ## Set temperature
    temperature_module.set_temperature(4)


    # exactly 5.2mm is 30ul of lysate in pcr
    aspirate_height = 5

    #right_pipette.pick_up_tip()
    #right_pipette.move_to(reagent_2ml_eppendorfs['A1'].bottom(10))
    #protocol.delay(seconds=8)
    #right_pipette.return_tip()

    dispense_well_list = ['A1', 'A2','A3','A4','A5','A6', 'A7', 'A8', 'A9', 'A10']

    for well in dispense_well_list:

        distribute_lysate(well, aspirate_height)
        aspirate_height -= 0.1


    # turn off temp module
    temperature_module.deactivate()


    # 10x to 50x

    # Row 1 to Row 2


    #right_pipette.transfer(300,
    # reagent_falcon_block.wells_by_name()['A1'],
    #  plate.columns_by_name()['7','8','9','10','11','12'],
    #  new_tip='never')
