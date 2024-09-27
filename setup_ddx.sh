#!/bin/bash

# Create subdirectories inside the current DDX folder
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/cache

mkdir -p src/data_pull
mkdir -p src/utils

mkdir -p alphas

mkdir -p config

mkdir -p tests

mkdir -p logs

mkdir -p notebooks

# Create initial files
touch requirements.txt

# Add a message to indicate success
echo "Project structure created successfully!"

