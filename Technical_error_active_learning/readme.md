# Introduction

Instructions for deploying the analysis environment and descriptions of the code and workflows within.


# Usage

1. Open command line and navigate to the unpacked directory

You can get the path by 'Copy address as text' in the URL of your file manager.
Be sure to stick the url in it's own quotes as below. This enters it as a string and will allow CMD to read any spaces in the path correctly.


```bash
cd "C://mypath/directory/my project/subfolder"
```

2. Build the docker image

```bash
docker build -t technical_error_analysis_docker_image .
```

3. Run your container on port 9998

Windows:
```bash
docker run -p 9998:8888 -v "%CD%":/app --name technical_error_analysis_docker_container technical_error_analysis_docker_image
```

If you're on Mac or Linux:

```bash
docker run -p 8888:8888 -v "%PWD":/app --name technical_error_analysis_docker_container technical_error_analysis_docker_image
```

The way it works is by:
a. starting a Docker Container
b. Mounting your current directory ("%CD%") to
a directory in the container ("/app") so that files can be shared and moved in and out.
c. starting a Jupyter server.

4. If it has started correctly, you'll get a url token. Copy the token provided into your brower URL

It should look like this:

`http://127.0.0.1:8888/?token=3c96d2a50decb4302c3e96b87ba7444d286e335d07c478fe`

It should open up a Jupyter File explorer in the directory in your browser.


# Experiment Diary

### ALTE001

10x replicates
First run of pipetting a lysate reaction.
Used Michael's reagents
Only one replicate worked.
Manually added the wax

### ALTE002

Repeat of ALTE001 but with automated waxing.
On the same plate as ATLE003.

### ALTE003

Same as ALTE002 but using Alex's lysate and ES as a positive control.
Will segregate the raw data files manually.


## Combined run

The pipetting script was improved to make it more dynamic and allow multiple experiments on one plate.

** Wax new tip should not be Never to avaoid cross contamination **

### ALTE006

As we had a load of trouble with ALTE005, having had to do multiple runs and seeing no signal -  To rule out MS lysate and substrates being a bit crap, we're doing a complete re-run but with AP lysate and substrates.

### ALTE007

We're also trialling sticking the substrates in first before the viscous lysate and seeing if that makes a difference. -  Used MS substrates
