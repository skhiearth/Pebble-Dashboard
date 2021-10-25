from flask import Flask
import pandas as pd
from dash import Dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from pandas.core.frame import DataFrame
import os
import pebble_pb2
import numpy as np
import requests
from .queryScript import run_query
import datetime

# Create the Dash app
app = Dash(external_stylesheets=[dbc.themes.FLATLY])
server = app.server
app.title = 'Pebble Dashboard'

query = """
{
  devices {
    id
    name
    address
    owner
    lastDataTime
    status
    name
    data
    config
  }
}
"""
result = run_query(query)

statusDf = pd.DataFrame(columns = ["Id", "Name", "Address", "Owner", "Last Data Time", "Last Data", "Status", "Raw Data",
                                  "Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", "Pressure",
                                  "Humidity", "Light", "Temperature2", "Gyroscope1", "Gyroscope2", "Gyroscope3", 
                                  "Accelerometer1", "Accelerometer2", "Accelerometer3"])

for key, value in result["data"].items():
    for device in value:
        data = []
        data.append(device["id"])
        data.append(device["name"])
        data.append(device["address"])
        data.append(device["owner"])
        data.append(device["lastDataTime"])
        
        if(device["lastDataTime"] == None):
            data.append("None")
        else:
            data.append(datetime.datetime.utcfromtimestamp(int(device["lastDataTime"])).strftime('%Y-%m-%d %H:%M:%S'))
            
        data.append(device["status"])
        
        if(device["data"]):
            dataString = device["data"].replace("0x", "")
            data.append(dataString)
            dataBytes = bytes.fromhex(dataString)
            sensorData = pebble_pb2.SensorData()
            sensorData.ParseFromString(dataBytes)
            
            data.append(sensorData.snr)
            data.append(sensorData.vbat)
            data.append(sensorData.latitude)
            data.append(sensorData.longitude)
            data.append(sensorData.gasResistance)
            data.append(sensorData.temperature)
            data.append(sensorData.pressure)
            data.append(sensorData.humidity)
            data.append(sensorData.light)
            data.append(sensorData.temperature2)
            if(len(sensorData.gyroscope) == 3):
                data.append(sensorData.gyroscope[0])
                data.append(sensorData.gyroscope[1])
                data.append(sensorData.gyroscope[2])
            else:
                data.append("No Data")
                data.append("No Data")
                data.append("No Data")
            if(len(sensorData.accelerometer) == 3):
                data.append(sensorData.accelerometer[0])
                data.append(sensorData.accelerometer[1])
                data.append(sensorData.accelerometer[2])
            else:
                data.append("No Data")
                data.append("No Data")
                data.append("No Data")
        else:
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            data.append("No Data")
            
        statusDf.loc[len(statusDf)] = data

statusDf.sort_values(by='Last Data Time', ascending = False, inplace=True)
statusDf.reset_index(inplace=True)
timeDf = statusDf[statusDf["Last Data"] != "None"]

timeDf['Latitude'] = timeDf['Latitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))
timeDf['Longitude'] = timeDf['Longitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))

timeDf["Longitude"] = pd.to_numeric(timeDf["Longitude"])
timeDf["Latitude"] = pd.to_numeric(timeDf["Latitude"])

timeDf['Last Data'] = pd.to_datetime(timeDf['Last Data'])
timeDf["Date"] = timeDf["Last Data"].dt.date

