from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <opentrons@example.com>',
    'description': 'Simple protocol to get started using the OT-2',
    'apiLevel': '2.12'
}

# protocol run function
def run(protocol: protocol_api.ProtocolContext):

    # labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location='1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', location='2')

    # pipettes
    left_pipette = protocol.load_instrument(
         'p300_single_gen2', mount='right', tip_racks=[tiprack])


    left_pipette.flow_rate.aspirate = 20
    left_pipette.flow_rate.dispense = 20

    # commands
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, plate['A1'])
    left_pipette.dispense(100, plate['D7'])
    left_pipette.dispense(100, plate['D8'])
    left_pipette.dispense(100, plate['D9'])
    left_pipette.drop_tip()
