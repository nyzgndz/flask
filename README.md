# Flask - Python Web Framework !

![Alt text](/flask.png?raw=true "Flask - Python Web Framework")

This repository includes complete example of **flask** web framework to show how to run a python script using web user interface. 

It consists of flask API service (flask_api.py), web user interface (index.html), custom JavaScript file in addition to bootstrap files, and some other miscellaneous files such as css, fonts, images etc..

### Example of the html index file:

![Alt text](/index.png?raw=true "Niog.Tech")

### Instructions:

- Clone / Download this repository
- I would recommend you to create **virtualenv** for this project. Otherwise, just install to requirements to your default python environment. To do that run the following command in the same directory.
> pip install -r requirements.txt
- Once you have required packages installed, you can run flask_api app to execute your commands using index.html.
> python flask_api.py
- Open **index.html**
- You can now query any thing using web UI. Please also check terminal while you are clicking the buttons. Some extra information were given for you! 

### Working Principle

Basically, whole idea is that transferring the required information from web user interface (**index.html**) to flask API, and let it to do the needed job. For this purpose, some buttons, textareas were created in the index.html (these have their values, names etc.). After that using **js/custom.js** JavaScript file, it is aimed to transfer information to flask_api.py. This custom JavaScript file constitutes the intermediate point between index.html and flask_api.py (transmits the information to each other). Finally, using **flask_api.py**, you can run `'your_python_code.py'` according to the information passed via custom JavaScript.

To sum up, if you want to change this for your own project, you just need to understand the logic in the following scripts. Modifying those scripts will help you to create your own project.

- index.html
- js/custom.js
- flask_api.py
- your_python_code.py (e.g. wikipedia_search.py)

## README for Running flask_api.py on Docker

1. Create docker image using ".Dockerfile" file. In order to do that, run the following command in the same directory in where all .Dockerfile is.
	$ docker build -t flask-example -f ./.Dockerfile .
	(NOTE: "flask-example" will be the docker repository name tag)

2. In order to see the image, type "docker images". You need to see "flask-example" in the list that docker images command returns.

3. Running on Docker
	$ docker run -it -p 5000:5000 --name running-image flask-example
	("running-image" will be the process name, which you can kill it with the following command later on.

		$ docker rm -f running-image

4. If you want to delete the image, type the following command

		$ docker rmi -f flask-example
