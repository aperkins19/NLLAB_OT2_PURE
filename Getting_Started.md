# Getting started

## Initial set up of the robot

First open the Opentrons application and turn the robot on. The blue light will
stop flashing and turn solid once the robot has paired with the computer. Once
it has paired the robot name should be listed and you can toggle it on. There
are a lot of settings that can be changed from the menus here.

## Setting up a protocol

Click on protocol and choose a file to upload. The scripts are written in
python for the Opentron. It will check a few things to do with the pipette and
tip calibrations and the labware set up. After these checks, click on proceed to
run where it will list a set of all the steps it will do in this protocol.
Finally click start run and watch as it performs the protocol.

## First protocol

The following example script was taken from the Opentron documentation. First
the protocol api is loaded from the opentrons package. After this, the metadata
is defined which includes protocol name, author, description, api level etc. The
protocol has to be defined in a run function and it must take exactly one
argument which is the protocol.

Inside the run function, the labware is defined first. The labware strings are
json files that have all the dimensions of the labware. The location of these
labware is also defined. On the floor of the Opentron there are numbers that
are the positions the labware can be placed. After this, the pipette is loaded
and tip rack is specified. Finally the commands are given to the robot. This
particular protocol tells it to pick a tip up from the tip rack at location 2,
aspirate 100ul from the well A1 on the 96 well plate at location 1, dispense
100ul into the well B2 on the 96 well plate and then drop the tip. 

``from opentrons import protocol_api

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
         'p300_single', mount='left', tip_racks=[tiprack])

    # commands
    left_pipette.pick_up_tip()
    left_pipette.aspirate(100, plate['A1'])
    left_pipette.dispense(100, plate['B2'])
    left_pipette.drop_tip()``
