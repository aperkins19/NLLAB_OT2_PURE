# Intro

Look at the powerpoint presentation for an overview of the workflow


# The Analysis

How to build and run a docker image that runs a Jupyter Server for the analysis.

Run the below code in a Command Line Interface.

## Navigate to the directory: /pipetting_accuracy_workflow/

`cd EXAMPLE_PATH/pipetting_accuracy_workflow/`

## Build the docker image

The build command will install the packages installed in requirements.txt

`docker build -t ot2_pipetting .`

## Run your container on port 8888

Windows:  
`docker run -p 8888:8888 -v "%CD%":/src --name ot2_pipetting_analysis_container ot2_pipetting `

If you're on Mac or Linux:

`docker run -p 8888:8888 -v "%PWD":/src --name ot2_pipetting_analysis_container ot2_pipetting`

## Access the notebooks


The way it works is by:
a. starting a Docker Container
b. Mounting your current directory ("%CD%") to a directory in the container ("/src") so that files can be shared and moved in and out.
c. starting a jupyter server.


You can then go to localhost:8888 on your browser and paste in the token given in the CLI output.  

If it has started correctly, you'll get a url token. Copy the token provided into your brower URL:  

It should look like this:`http://127.0.0.1:8888/?token=3c96d2a50decb4302c3e96b87ba7444d286e335d07c478fe`  

It should open up a Jupyter File explorer in the directory in your browser.
