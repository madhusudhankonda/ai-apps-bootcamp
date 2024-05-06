# Software Engineer's Bootcamp: Developing AI Powered Applications

Software Engineer's Bootcamp: Developing AI Applications 

# Pre-requisites

- [ ] Obtaining OpenAI API Key 
- [ ] Downloading Visual Studio Code (or any other IDEs)

# Check our this repo for your reference

Visit my [GitHub](https://github.com/madhusudhankonda) to clone the [template github](https://github.com/mkonda-ai-templates/template-openai) repository.

`git clone https://github.com/mkonda-ai-templates/template-openai.git ai-demo`

The cd into the `ai-demo` folder


# Check our the template repo

Visit my [GitHub](https://github.com/madhusudhankonda) to clone the [template github](https://github.com/mkonda-ai-templates/template-openai) repository.

`git clone https://github.com/mkonda-ai-templates/template-openai.git ai-demo`

The cd into the `ai-demo` folder


# Setting up Python virtual environment 

You have two options to setup a python env (I'm using `pip` for this setup)

1. You can use the provided `setup.sh` script to set your Python Virtual Environment if needed
2. You can manually create the `venv`

Here are the both types of instructions (follow what ever is convenient for you):

## Setting up the Python Env using a script

The project has a setup file - all you have to do is execute the script:

```
# Execute the script
. ./setup.sh
```

Executing the above script will 
 - Create a virtual environment automatically 
 - Once the venv was setup, it'll make sure the venv gets activated 
 - The requirements file gets invokes to install the required modules

## Setting up Python virtual environment manually

You can setup your Python virtual env manually as the instructions below demonstrate:

```
# Creating the virtual env

python -m venv .venv
```
Executing this command would create a virtual environmnet with a name `.venv`. The next step is to make sure we activate it.

Ensure the following command gets executed for the `venv` to get activated:

```
# Activating the Virtual Environment

source .venv/bin/activate
```

This command activates the virtual env. You can also issue `deactivate` if you'd want the venv to be shutdown.

Now that we have the env ready, let's install the dependencies.


# Installing the dependencies

The dependencies for this project are provided in the `requirements.txt` file.

```
# Installing the dependencies

pip install -r requirements.txt
```

Executing the above command should get the dependencies installed. 

# Open AI Key

We can set the OPENAI_API_KEY in multiple ways - preferred is to use `.env` in the root folder, holding the keys and other sensitive info. 

For this example, we simple set the key as an environment variable:

``` 
export OPENAI_API_KEY="<your-api-key>"
```

That's pretty much the information on setting up the project for working through this Bootcamp.

Let's dive into individual projects to get through the fundamentals - let's begin our journey into the world of AI.

## Chapter 1: OpenAI Basics

![OpenAI Basics](https://github.com/madhusudhankonda/ai-apps-bootcamp/blob/main/1_openai-basics/readme.md)

## Chapter 2: Introducing LangChain

## Chapter 3: OpenAI Basics


