#!/bin/bash

# Create a virtual environment named ".venv" in the current directory
python3 -m venv .venv

echo "Virtual environment created successfully!"

# Activate the virtual environment (uncomment if desired)
source .venv/bin/activate

# Install langflow

python -m pip install langflow -U
