# Import libraries
from json import load
from .server import *
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Import styles
from .style import *

# ---COMPONENTS---

# Load the dataset
sensor = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3("Sensor Analytics", style=HEADING)))),
        html.H5("Intelligent insights derived from current data to get sense of current health of devices"),
        dcc.Store(id='sensorData'),
        html.Div(id='in-load-sensor'),

        html.Hr(),
        html.H4("Signal-to-noise ratio"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="snrmin")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="snrmax")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="snrmean")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="snrmedian")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="snrmode")),
                ], style=COLUMN),
            ]
        ),

        html.Hr(),
        html.H4("Battery Voltage"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="vbatmin")),
                    html.H5(html.Center("Volts")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="vbatmax")),
                    html.H5(html.Center("Volts")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="vbatmean")),
                    html.H5(html.Center("Volts")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="vbatmedian")),
                    html.H5(html.Center("Volts")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="vbatmode")),
                    html.H5(html.Center("Volts")),
                ], style=COLUMN),
            ]
        ),
    ]
)

@app.callback(
    Output("snrmin", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Snr"].min())

@app.callback(
    Output("snrmax", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Snr"].max())

@app.callback(
    Output("snrmean", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(round(timeDf["Snr"].mean(), 2))

@app.callback(
    Output("snrmedian", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(round(timeDf["Snr"].median(), 2))

@app.callback(
    Output("snrmode", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Snr"].mode()[0])

@app.callback(
    Output("vbatmin", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Vbat"].min())

@app.callback(
    Output("vbatmax", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Vbat"].max())

@app.callback(
    Output("vbatmean", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(round(timeDf["Vbat"].mean(), 2))

@app.callback(
    Output("vbatmedian", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(round(timeDf["Vbat"].median(), 2))

@app.callback(
    Output("vbatmode", component_property='children'), 
    Input('sensorData', 'data'))
def update_line_chart(data):
    return "{}".format(timeDf["Vbat"].mode()[0])