import requests
import pandas as pd
import numpy as np
import pebble_pb2
import datetime
import json
from .queryScript import run_query

def getDeviceData(imei):
    query = """
    {
      deviceRecords(where: { imei: "%s" }) {
        raw
        imei
        signature
        timestamp
      }
    }
    """ %(imei)

    result = run_query(query)

    deviceDf = pd.DataFrame(columns = ["Id", "Timestamp", "Raw Data", "Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", 
                                       "Pressure", "Humidity", "Light", "Temperature2", "Gyroscope1", "Gyroscope2", "Gyroscope3", 
                                      "Accelerometer1", "Accelerometer2", "Accelerometer3"])

    for key, value in result["data"].items():
        for subkey in value:
            data = []
            data.append(imei)

            if((subkey['raw'] != "0x") and (subkey['raw'])):
                dataString = subkey['raw'].replace("0x", "")
                data.append(datetime.datetime.utcfromtimestamp(int(subkey["timestamp"])).strftime('%Y-%m-%d %H:%M:%S'))
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
                data.append("No Data")

            deviceDf.loc[len(deviceDf)] = data

    deviceDf['Latitude'] = deviceDf['Latitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))
    deviceDf['Longitude'] = deviceDf['Longitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))

    deviceDf["Longitude"] = pd.to_numeric(deviceDf["Longitude"])
    deviceDf["Latitude"] = pd.to_numeric(deviceDf["Latitude"])

    deviceDf.sort_values(by='Timestamp', ascending = False, inplace=True)
    deviceDf.reset_index(inplace=True)
    
    return deviceDf