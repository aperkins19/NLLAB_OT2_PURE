# Intro

This document contains the experimental design, planning and technical decisions for the OT2 technical error reducing AL experiments.

# Premise

The aim is to use AL to optimise the technical error between replicates by modulating:

* Aspirate / Dispensing speeds
* Aspirate / Dispensing Pipette tip height  ** Looks like dispense volume is absolutely key for low volumes **
* Reverse pipetting


# Design

* 10x *E. coli* lysate + pBest reactions per each config set.
* We will use Michael's standard reaction composition.


# Initialising the settings

## Aspiration height

Using the information above:

2.5ul of lysate x 10 = 25ul
Adding a bit extra = 30ul.

The meniscus height of 30ul in a PCR tube is around 5mm above the bottom


# Experiments

## 1. Checking lysate pipetting in PCR Tubes

Pipetted 10x 2.5ul in to 10x PCR tubes at 4 degrees.

`    # first laydown the lysate
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
    temperature_module.deactivate()`

  We observed lysate in every target PCR tube - technical error unknown.

## Pipetting lysate into a 384 well plate
