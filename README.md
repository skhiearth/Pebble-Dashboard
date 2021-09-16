# Pebble Dashboard
Source code for the IoTeX Pebble Tracker dashboard by The Misfits for Grants Round 11 Hackathon by Gitcoin and IoTeX 

Access the dashboard [here](https://pebble-dashboard.herokuapp.com/)

### WHAT IT DOES? 

The Pebble Analytics dashboard provides an interactive way to monitor activity of pebble devices on the network. Using the TruStream network, this is a decentralised and trustless way of observing all devices on the network. Various sensor parameters are tracked and represented.

### DATA SOURCES

TruStream's Subgraph Endpoint

### TECHNICAL IMPLEMENTATION

The dashboard follows the UI aesthetic of the IoTT portal web application and due to integration of Bootstrap, it is responsive on mobile and smaller devices.

![Technical framework](https://raw.githubusercontent.com/skhiearth/Pebble-Dashboard/main/Implementation.jpg)

### Requirements

#### Hardware

* Mac, Linux or Windows (MacOS preffered)
* Atleast 4GB of RAM recommended 

#### Software

* Python 3.7+
* Pip Package Manager

#### Instructions

Clone the GitHub repo on your local machine. Navigate to the project folder in the terminal and run ` pip install -r requirements.txt` to install dependencies. Open the workspace in a code editor of choice and run the `app.py` file. Navigate to `http://127.0.0.1:8050/` (or your default location) in your browser to access alocal version of the dashboard or navigate to `https://pebble-dashboard.herokuapp.com/` to access a live version.

