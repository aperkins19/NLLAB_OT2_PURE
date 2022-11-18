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

# Connecting to OT2 through ssh

## Generating key pair
```bash
ssh-keygens
```

## Sending public key to raspberry pi

### Command template - This needs to be ran in Powershell
@{key = Get-Content [ssh key file path] | Out-String} | ConvertTo-Json | Invoke-WebRequest -Method Post -ContentType 'application/json' -Uri [OT2 ip]:31950/server/ssh_keys -UseBasicParsing


```bash
@{key = Get-Content C:\users\s1530400\.ssh\id_rsa | Out-String} | ConvertTo-Json | Invoke-WebRequest -Method Post -ContentType 'application/json' -Uri 169.254.156.218:31950/server/ssh_keys -UseBasicParsing
```

## Transferring a file over

### Note!!!
Can't transfer files from M:\ datastore folder path for some reason. Transfer files from C:\.

### Command template
scp -i [ssh key file path] [file_path_from_local] root@[OT2 IP (may change - find in OT2 UI)]:[file_path_on_ot2]

```bash
scp -i C:\users\s1530400\.ssh\id_rsa C:\users\s1530400\NLLAB_OT2_Protocol_Dev\Technical_error_active_learning\src\OT2_scripts\OT2_settings\test.json root@169.254.156.218:/data/user_storage/al_cell_free
```

## Transferring a folder over

### Command template
scp -r -i [ssh key file path] [file_path_from_local] root@[OT2 IP (may change - find in OT2 UI)]:[file_path_on_ot2]

### This example transfers a whole folder called ALTE007 which contains the protocol .py file, the experiment settings json file,
### the labware settings json file and the pipetting settings json files
```bash
scp -r -i C:\users\nllab_ot2\.ssh\ot2_ssh_key C:\users\nllab_ot2\NLLAB_OT2_Protocol_Dev\Technical_error_active_learning\src\OT2_scripts\ALTE007\ root@169.254.156.218:/data/user_storage/
```

## Connecting to the OT2 raspberry pi
ssh -i ot2_ssh_key root@[OT2 IP]

```bash
ssh -i C:\Users\nllab_ot2\.ssh\ot2_ssh_key root@169.254.156.218
```

## Running the protocol from the command line (on raspberry pi)
```bash
opentrons_execute ALTE007_technical_error_AL_pipetting_script.py
```
