# mygpt# template-openai-langchain

This template combines OpenAI and Langchain

> You must have a OpenAI Key as a pre-requisite


# Setting up Python virtual environment via script

You can use the provided `setup.sh` script to set your Python Virtual Environment if needed:

```
# Setting up the Python Env using a script

```
# Execute the script
. ./scripts/setup.sh
```

Executing the above script will create a virtual environment automatically. 

# Setting up Python virtual environment manually

You can setup your Python virtual env manually as the instructions below demonstrate:
```
# Creating the virtual env

python -m venv .venv
```

```
# Activating the Virtual Env

source .venv/bin/activate
```

# Installing the dependencies

The dependencies for this project are provided in the `requirements.txt` file.

```
# Installing the dependencies

pip install -r requirements.txt
```

Executing the above command should get the dependencies installed. 

# Running the app using Streamlit

Issue the following command to run the server using Streamlit:

```
streamlit run /src/main.py
```
This will usually start the server on `http://localhost:8501` - access this application by clicking on this link.

> Make sure the Ollama is running on your local machine. If the Ollama is not running, you'll encounter Http Connection issue. 

This should bring up your application in your local environment. Remember, the Ollama server must be up and running on your machine.

# Dockerising the App

In addition to the locally running the application, it can be dockerised too. Let's see this action in the following section.

## Building user Docker

First step is to build the app - you can build the app's image separately by executing the following command:

```
docker build -t mygpt:0.1 .
```

This will produce a docker image mygpt:0.1 which is referenced in the docker-compose file. 

Note the `.` at the end of the command - it is to indicate the current folder to be used as the build's input.


## The `.env` file

The `docker compose` command expects the environment file to load a few propertis such as MODEL, OLLAMA_BASE_URL etc. If it doesn't exist, make sure the `.env` file exists in the current directory 

Make sure the env file has the `OLLAMA_BASE_URL`, `MODEL` and `MODEL_VERBOSE` attributes. 

Take a copy of `.env_sample` and rename it to `.env` and change the attribute values as per your requirements.

When running the app in your local environment, the `OLLAMA_BASE_URL` must be set to localhost, like shown following:

```
OLLAMA_BASE_URL=http://localhost:11434

```

However, if you are running in a container, uncomment the following property to use "ollama" as the service:

```
OLLAMA_BASE_URL=http://ollama:11434
```

You can also add `MODEL_VERBOSE=True` attribute to the `.env` file so the models spit out logging information, as shown below:

```
MODEL_VERBOSE=True
```

Once the image is created successfully, you can run the app by issuing the following command:


# Running the app via Docker

We can run the same application using docker. By running the app in docker, we are combining both Ollama sever and our app to run simultaneously in the docker env (see the `docker-composer.yml` file to learn the composure of these two services).

Issue the following command:

```
docker compose --env-file .env up
```

The docker-compose.yml file has two services - the ollama and mygpt - both will be composed and executed.

# Accessing your application

The app is available on https://localhost:8501
