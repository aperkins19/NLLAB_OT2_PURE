# Intro

This subsection deals with calibrating the OT2 for different liquids.  
This is important for pipetting accurately and keeping technical error to a minimum.  
Liquids of different viscosities and surface tensions will require different settings e.g.:

* Aspirate / Dispensing speeds
* Pipette tip submersion in liquid source whilst aspirating. Especially important for low volumes (0.1ul on the outside of the tip is 10% of a 1ul pipetting step).
* tip_touch()?
* reverse pipetting?

# Project Map:

## liquid_volumes_mm.csv

This file contains the dataset for the liquid volume : miniscus relationship as measured with calipers.

## /pipetting_accuracy_workflow/

This directory contains the scripts, .csv file and analysis notebook for characterising each liquid.

To perform analysis, run the jupyter notebook using the dockerfile via the documentation given in the readme.txt
