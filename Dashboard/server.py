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
print("TESSSST")
print(result)

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

timeDf = timeDf.replace(to_replace="No Data", value = 0)

timeDf["Snr"] = pd.to_numeric(timeDf["Snr"])
timeDf["Snr"] = timeDf["Snr"] / 100
timeDf['Snr'] = timeDf['Snr'].round(2)

timeDf["Vbat"] = pd.to_numeric(timeDf["Vbat"])
timeDf["Vbat"] = timeDf["Vbat"] / 100
timeDf['Vbat'] = timeDf['Vbat'].round(2)

timeDf["Gas Resistance"] = pd.to_numeric(timeDf["Gas Resistance"])
timeDf["Gas Resistance"] = timeDf["Gas Resistance"] / 100
timeDf['Gas Resistance'] = timeDf['Gas Resistance'].round(1)

timeDf["Temperature"] = pd.to_numeric(timeDf["Temperature"])
timeDf["Temperature"] = timeDf["Temperature"] / 100
timeDf['Temperature'] = timeDf['Temperature'].round(1)

timeDf["Temperature2"] = pd.to_numeric(timeDf["Temperature2"])
timeDf["Temperature2"] = timeDf["Temperature2"] / 100
timeDf['Temperature2'] = timeDf['Temperature2'].round(1)

timeDf["Pressure"] = pd.to_numeric(timeDf["Pressure"])
timeDf["Pressure"] = timeDf["Pressure"] / 100
timeDf['Pressure'] = timeDf['Pressure'].round(1)

timeDf["Humidity"] = pd.to_numeric(timeDf["Humidity"])
timeDf["Humidity"] = timeDf["Humidity"] / 100
timeDf['Humidity'] = timeDf['Humidity'].round(1)

timeDf["Light"] = pd.to_numeric(timeDf["Light"])
timeDf["Light"] = timeDf["Light"] / 100
timeDf['Light'] = timeDf['Light'].round(1)

timeDf["Gyroscope1"] = pd.to_numeric(timeDf["Gyroscope1"])
timeDf["Gyroscope1"] = timeDf["Gyroscope1"] / 100
timeDf['Gyroscope1'] = timeDf['Gyroscope1'].round(1)

timeDf["Gyroscope2"] = pd.to_numeric(timeDf["Gyroscope2"])
timeDf["Gyroscope2"] = timeDf["Gyroscope2"] / 100
timeDf['Gyroscope2'] = timeDf['Gyroscope2'].round(1)

timeDf["Gyroscope3"] = pd.to_numeric(timeDf["Gyroscope3"])
timeDf["Gyroscope3"] = timeDf["Gyroscope3"] / 100
timeDf['Gyroscope3'] = timeDf['Gyroscope3'].round(1)

timeDf["Accelerometer1"] = pd.to_numeric(timeDf["Accelerometer1"])
timeDf["Accelerometer1"] = timeDf["Accelerometer1"] / 100
timeDf['Accelerometer1'] = timeDf['Accelerometer1'].round(1)

timeDf["Accelerometer2"] = pd.to_numeric(timeDf["Accelerometer2"])
timeDf["Accelerometer2"] = timeDf["Accelerometer2"] / 100
timeDf['Accelerometer2'] = timeDf['Accelerometer2'].round(1)

timeDf["Accelerometer3"] = pd.to_numeric(timeDf["Accelerometer3"])
timeDf["Accelerometer3"] = timeDf["Accelerometer3"] / 100
timeDf['Accelerometer3'] = timeDf['Accelerometer3'].round(1)

timeDf['Last Data'] = pd.to_datetime(timeDf['Last Data'])
timeDf["Date"] = timeDf["Last Data"].dt.date

