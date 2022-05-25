

6. Build the docker image

""
docker build -t ot2_pipetting .
""

7. Run your container on port 8888
e.g.

""
docker run -p 9999:8888 -v "%CD%":/src ot2_pipetting
""

If you're on Mac or Linux:

""
docker run -p 8888:8888 -v "%PWD":/src ot2_pipetting
""


If the image isn't already on your machine, it'll be downloaded.

The way it works is by:
a. starting a Docker Container
b. Mounting your current directory ("%CD%") to a directory in the container ("/src") so that files can be shared and moved in and out.
c. starting a jupyter server.





6. If it has started correctly, you'll get a url token. Copy the token provided into your brower URL

It should look like this:

""
http://127.0.0.1:8888/?token=3c96d2a50decb4302c3e96b87ba7444d286e335d07c478fe
""

It should open up a Jupyter File explorer in the directory in your browser.


7. Move your rawdata file (.CSV) into the directory and check it's appeared in the Jupyter directory.

8. Open bradforddataprocessing.ipynb and execute all cells using the double arrow icon.

9. It will create an output directory, move the raw data file into it, perform the analysis and put the products into the output directory.
You can now move the output directory out and put it where ever you like.

10. Shutdown Jupyter by CTRL-C and typing 'y' ENTER when prompted.

