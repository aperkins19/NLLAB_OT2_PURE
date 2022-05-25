from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Bradford Platting. V.001',
    'author': 'Alex Perkins',
    'email': 'a.j.p.perkins@sms.ed.ac.uk',
    'description': 'Simple protocol to plate a bradford assay - not dynamic',
    'apiLevel': '2.11'
}


# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '5')

    reagent_falcon_block = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','8')
    reagent_2ml_eppendorfs = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', '6')


    # pipettes
    tiprack_20ul = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    left_pipette = protocol.load_instrument(
         'p20_single_gen2', 'left', tip_racks=[tiprack_20ul])

    tiprack_300ul = protocol.load_labware('opentrons_96_tiprack_300ul', '11')
    right_pipette = protocol.load_instrument(
         'p300_single_gen2', 'right', tip_racks=[tiprack_300ul])


    #    commands

    # Dilutions

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

    # exactly 50mm is 6.5ml on 15ml falcon
    aspirate_height = 40

    #right_pipette.pick_up_tip()
    #right_pipette.move_to(reagent_2ml_eppendorfs['A1'].bottom(10))
    #protocol.delay(seconds=8)
    #right_pipette.return_tip()

    dispense_well_list = ['A1', 'A2', 'A3', 'A4', 'A5']

    for well in dispense_well_list:

        distribute_bradford_reagent(well, aspirate_height)
        aspirate_height -= 2


    # 10x to 50x

    # Row 1 to Row 2


    #right_pipette.transfer(300,
    # reagent_falcon_block.wells_by_name()['A1'],
    #  plate.columns_by_name()['7','8','9','10','11','12'],
    #  new_tip='never')
