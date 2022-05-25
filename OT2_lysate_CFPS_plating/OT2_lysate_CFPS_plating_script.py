from opentrons import protocol_api
import numpy as np

# metadata
metadata = {
    'protocolName': 'SBSG Lysate CFPS OT2 Plating Script',
    'author': 'Alex Perkins',
    'email': 'a.j.p.perkins@sms.ed.ac.uk',
    'description': 'SBSGs basic script for plating out lysate CFPS reactions.',
    'apiLevel': '2.11'
}




# protocol run function
def run(protocol: protocol_api.ProtocolContext):

    # labware
    nunc_384_flat = protocol.load_labware('corning_384_wellplate_112ul_flat', location='4')

    # config file uploaded to OT2 app in custom labware
    pcr_tube_rack = protocol.load_labware('starlabpcrwsstrips_96_wellplate_200ul', location='8')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', location='2')

    # pipettes
    p20_pipette = protocol.load_instrument(
         'p20_single_gen2', mount='left', tip_racks=[tiprack_1])


    # Custom commands

    def distribute_energy_solution_and_dna_mix(aspirate_well, dispense_well, aspirate_height, dispense_volume):


        if dispense_volume == 0:
            pass

        else:

            aspirate_volume = dispense_volume

            p20_pipette.aspirate(aspirate_volume, aspirate_well)
            p20_pipette.dispense(dispense_volume, dispense_well)


            #protocol.comment(str(aspirate_well))
            #protocol.comment(str(dispense_well))
            #protocol.comment(str(dispense_volume))


    # Run

    aspirate_wells = [pcr_tube_rack['A1']] * 96

    # In this 2d array, each dim is a row.
    # The array is then reshaped to flatten to 1D columnwise starting from A1 to P1...A2...P2 etc

    dispense_volumes = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    # the flatten command
    dispense_volumes = dispense_volumes.ravel(order="F")


    aspirate_height = 5


    p20_pipette.pick_up_tip()

    # iterates over the wells and is passed pipetting volumnes

    for aspirate_well, dispense_well, dispense_volume in zip(aspirate_wells, nunc_384_flat.wells(), dispense_volumes):

        distribute_energy_solution_and_dna_mix(aspirate_well, dispense_well, aspirate_height, dispense_volume)

    p20_pipette.drop_tip()
