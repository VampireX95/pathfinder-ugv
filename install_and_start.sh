#!/bin/bash

# Update system
#echo "Updating system..."
#sudo apt update && sudo apt upgrade -y
#
## Install Python 3, pip, and necessary libraries
#echo "Installing required packages..."
#sudo apt install -y python3-pip python3-dev python3-venv libatlas-base-dev picamera
#
## Navigate to the project directory
#cd "$(dirname "$0")"
#
## Create a Python virtual environment
#echo "Creating a virtual environment..."
#python3 -m venv venv
#
## Activate the virtual environment
#echo "Activating virtual environment..."
source venv/bin/activate

# Install required Python packages
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Start the Flask app in the background using nohup
echo "Starting Flask app..."
python3 app.py

# Confirm the Flask app is running
echo "Flask app started in the background. You can access it at http://<Raspberry_Pi_IP>:5000"
