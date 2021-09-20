# Import libraries
from json import load
from os import stat
from .server import *
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Import styles
from .style import *

# ---COMPONENTS---
overview = html.Div(
    [
        dbc.Row([
            dcc.Store(id='statusData'),
            html.Div(id='in-load'),
            dbc.Col(html.Div(html.H3("Overview", style=HEADING))),
        ]),
        html.Hr(),

        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H4("Devices"),
                    html.P(),
                    html.H5(id='totalDevices'),
                    html.H5(id='confirmedDevices'),
                    html.H5(id='pendingDevices'),
                    html.H5(id='activeData'),
                    html.H5(id='noData'),
                ], style=COLUMN),
                dbc.Col([
                    html.H4("Users with most devices"),
                    html.P(),
                    html.H5(id='firstDevices'),
                    html.H5(id='secondDevices'),
                    html.H5(id='thirdDevices'),
                ], style=COLUMN),
            ]
        ),

        html.Hr(),

        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H4("Pebble tracker with latest update"),
                    html.H6("This pebble tracker has sent the latest data update to the TruStream network out of all registered trackers"),
                    html.P(),
                    html.H5(id='timeLatest'),
                    html.H5(id='idLatest'),
                    html.H5(id='nameLatest'),
                    html.H5(id='addressLatest'),
                    html.H5(id='ownerLatest'),
                ], style=COLUMN),
                dbc.Col([
                    html.H4("Pebble tracker with oldest update"),
                    html.H6("This pebble tracker has not sent a data update to the TruStream network in the longest time out of all registered trackers"),
                    html.P(),
                    html.H5(id='timeOldest'),
                    html.H5(id='idOldest'),
                    html.H5(id='nameOldest'),
                    html.H5(id='addressOldest'),
                    html.H5(id='ownerOldest'),
                ], style=COLUMN),
            ]
        ),
    ]
)

# Cards
# Devices
@app.callback(
    Output("totalDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Total Devices: {}".format(len(statusDf))

@app.callback(
    Output("confirmedDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Confirmed Devices: {}".format(len(statusDf[statusDf["Status"] == 2]))

@app.callback(
    Output("pendingDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Pending Devices: {}".format(len(statusDf[statusDf["Status"] == 1]))

@app.callback(
    Output("activeData", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Active Devices: {}".format(len(statusDf[statusDf["Raw Data"] != "No Data"]))

@app.callback(
    Output("noData", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Devices with no data yet: {}".format(len(statusDf[statusDf["Raw Data"] == "No Data"]))


# Owner Frequency
@app.callback(
    Output("firstDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[0],
    statusDf.Owner.value_counts()[:4].index.tolist()[0])

@app.callback(
    Output("secondDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[1],
    statusDf.Owner.value_counts()[:4].index.tolist()[1])

@app.callback(
    Output("thirdDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[2],
    statusDf.Owner.value_counts()[:4].index.tolist()[2])


# Oldest/Latest
@app.callback(
    Output("timeLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Time: {}".format(timeDf.iloc[0]["Last Data"])

@app.callback(
    Output("timeOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Time: {}".format(timeDf.iloc[-1]["Last Data"])

@app.callback(
    Output("idLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "ID: {}".format(timeDf.iloc[0]["Id"])

@app.callback(
    Output("idOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "ID: {}".format(timeDf.iloc[-1]["Id"])

@app.callback(
    Output("nameLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Name: {}".format(timeDf.iloc[0]["Name"])

@app.callback(
    Output("nameOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Name: {}".format(timeDf.iloc[-1]["Name"])

@app.callback(
    Output("addressLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Address: {}".format(timeDf.iloc[0]["Address"])

@app.callback(
    Output("addressOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Address: {}".format(timeDf.iloc[-1]["Address"])

@app.callback(
    Output("ownerLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Owner: {}".format(timeDf.iloc[0]["Owner"])

@app.callback(
    Output("ownerOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Owner: {}".format(timeDf.iloc[-1]["Owner"])