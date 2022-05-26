

# 25th May

## Completed
* Set up temperature module
* Characterise handling lysate. Create a script to try different parameters
and see the technical error. **We tried doing this by weighing pcr tubes before
and after using the chemical balance but the volumes (~2.5ul doesn't weigh enough
for the instument to capture the error. We have decided to proceed straight to the
CFPS reaction and use variance between technical replicates as a proxy for
pipetting error.**
* Get the Opentron to consistently pipette lysate into 10 pcr tubes. Need to make sure
we get the aspiration height and dispense height correct. We can set this up to work
for 30ul of lysate in a pcr tube. Unfortunately, we can't measure this from weighing
the tubes as the volumes are too small. May need to check this by eye and then we
can keep track of the error by using the technical error from the plate reader reactions.
If this technical error is small then the lysate distribution must be pretty consistent.
We decided to move onto just pipetting into the 384 well plate and optimising that
rather than optimising it for pipetting into pcr tubes.


## To do
* Set up first lysate reaction with OT2
* Get the Opentron to distribute lysate onto the 384 well plate - 10 replicates.
This seems to be working now, however, we have been having issues with the calibration
of the opentron. It seems to be off by about 1 mm in the z axis and x axis (it
is off when picking up a tip even after calibrating.) !!!Need to do a factory reset
when picking this up tomorrow!!!!
* Get the Opentron to make a master mix of energy solution, dna, (malachite green),
chi6, buffer, water. This could be a separate script.
