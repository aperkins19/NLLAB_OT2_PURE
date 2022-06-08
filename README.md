# Protocol development for OT2 Opentron


# Project Planning & Management


## 07/06/2022

### Run by MS

* Ran 10 replicates of pbest DNA on opentron with MS lysate 1 and MS Energy Solution 001.
* 2 replicates (towards the end) never got any master mix - need to increase the substrate aspiration height increment
* Made a mistake and put well plate back on opentron in wrong place after spinning so did wax step myself.
* Only measuring GFP for 12 hours.

## Bug fixes by AP
Changed preprocessing scripts to:
* cope better with different types of time lists.
* rearrange the header metadata in "_raw.csv" so we don't have to do it manually
* fixed the processing of ALTE004 and produced the plots.
#### Question for Michael - have you updated the energy solution height increment post ALTE004?  LMK

## 30/05/2022

* Changed robot level and recalibrated. Offset seems to be reduced but still occurs. Have discovered that you can, in fact, run a 'Labware Offset Check' when setting up the deck to run a protocol.
This allows you to tell robot exactly where the bits of labware are and seems to correct the offset. See pipette_offset_data.png in this directory for correction data. This appears to have fixed the problem.

* Run another 10x 2.5ul lysate check: Better ! But pipetting destination in the well is a little inconsistent but maybe this is due to variable pipette curvatures / mounting angles on the pipette.

* Probably good enough to continue to a first CFPS run.

## To do  - Near term

* Put all pipetting parameters into a dictionary

* Install Black

* Get the Opentron to make a master mix of energy solution, dna, (malachite green),
chi6, buffer, water. This could be a separate script, *or a modular function that can simply be called upstream of the plating functions*. AP

* Design the technical error optimiser - once we have our 1st 10x cfps replicated. let's sit down with pen, paper and coffee and design the algorithm + software plan next week. AP

* Code wax pipette step and fix pipette
  * OT2 parts.
    * Insert sink plugs into 3D printed tube rack with Mirren.
    * Confirm dimensions + build quality
    * Order rest of parts from U create.

## To do - Far term

* **Recalibration**  Get the Opentron to distribute lysate onto the 384 well plate - 10 replicates.
This seems to be working now, however, we have been having issues with the calibration
of the opentron. It seems to be off by about 1 mm in the z axis and x axis (it
is off when picking up a tip even after calibrating.)
  * Alex has brought in his spirit level - use this to ensure the OT2 is level by adjusting feet.
  * Need to do a factory reset

* Run successive rounds of technical error reduction active learning.

* Design 3D printed PCR tube rack


### Completed

* ~create /app in linux of docker~
* ~Set up first lysate reaction with OT2~
* ~Set up temperature module~
* ~Characterise handling lysate. Create a script to try different parameters
and see the technical error. **We tried doing this by weighing pcr tubes before
and after using the chemical balance but the volumes (~2.5ul doesn't weigh enough
for the instument to capture the error. We have decided to proceed straight to the
CFPS reaction and use variance between technical replicates as a proxy for
pipetting error.**~
* ~Get the Opentron to consistently pipette lysate into 10 pcr tubes. Need to make sure
we get the aspiration height and dispense height correct. We can set this up to work
for 30ul of lysate in a pcr tube. Unfortunately, we can't measure this from weighing
the tubes as the volumes are too small. May need to check this by eye and then we
can keep track of the error by using the technical error from the plate reader reactions.
If this technical error is small then the lysate distribution must be pretty consistent.
We decided to move onto just pipetting into the 384 well plate and optimising that
rather than optimising it for pipetting into pcr tubes.~
