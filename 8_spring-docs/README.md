# spring-docs
Spring Framework Docs Assistant

# Building user Docker

You can build the app's image separately by executing the following command:
```
docker build -t spring-docs:0.1 .
```

This will produce a docker image spring-docs:0.1 which is referenced in the docker-compose file. Hence, you can run the app by issuing the following command:

```
# Running the docker compose

docker compose --env-file .env up 
```

Make sure the `.env` file exists in the current directory.

## Env file

Make sure the env file has the following attributes:

```
# Use this URL is you are running using streamlit run command:
# OLLAMA_BASE_URL=http://localhost:11434

# If running in a container, use "ollama" as the sevice
OLLAMA_BASE_URL=http://ollama:11434

MODEL=codellama
MODEL_VERBOSE=True
```
> You can take a copy of `.env_sample` and rename it to `.env` and change the attribute values as per your requirements

# Running the app using Streamlit

Issue the following command to run the server using Streamlit:

```
streamlit run /src/main.py
```
This will usually start the server on `http://localhost:8501` - access this application by clicking on this link.

> Make sure the Ollama is running on your local machine. If the Ollama is not running, you'll encounter Http Connection issue. 

# Running the app via Docker

We can run the same application using docker. By running the app in docker, we are combining both Ollama sever and our app to run simultaneously in the docker env (see the `docker-composer.yml` file to learn the composure of these two services).

Issue the following command:

```
docker compose --env-file .env up
```