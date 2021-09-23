# Import libraries
from json import load
from os import defpath
from .server import *
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .getDeviceData import getDeviceData

# Import styles
from .style import *

# ---COMPONENTS---
ids = timeDf.Id.unique()

device = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3("Device Analytics", style=HEADING)))),
        dcc.Store(id='deviceData'),
        html.Div(id='in-load'),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': i, 'value': i} for i in ids
            ], value=ids[0]
        ),

        dbc.Row(children=[
                dbc.Col([
                    html.H4("Overview"),
                    html.H6("Generic metadata about this particular Pebble tracker"),
                    html.P(),
                    html.P(),
                    html.H5(id='idLatestPebble'),
                    html.H5(id='timeLatestPebble'),
                    html.H5(id='nameLatestPebble'),
                    html.H5(id='addressLatestPebble'),
                    html.H5(id='ownerLatestPebble'),
                ], style=COLUMN)
            ]
        ),

        html.Hr(),
        html.H4("Current Data"),
        html.H6("Latest data sent by this pebble tracker"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(id='snr'),
                    html.H5(id='vbat'),
                    html.H5(id='latitude'),
                    html.H5(id='longitude'),
                    html.H5(id='gasResistance'),
                    html.H5(id='temperature'),

                ], style=COLUMN),
                dbc.Col([
                    html.H5(id='pressure'),
                    html.H5(id='latitude'),
                    html.H5(id='longitude'),
                    html.H5(id='gasResistance'),
                    html.H5(id='humidity'),
                    html.H5(id='light'),
                ], style=COLUMN),
            ]
        ),

        dbc.Row(children=[
                dbc.Col([
                    html.H5("Latest Gyroscope Readings"),
                    html.H6(id='gyroscope'),
                ], style=COLUMN),
                dbc.Col([
                    html.H5("Latest Accelerometer Readings"),
                    html.H6(id='accelerometer'),
                ], style=COLUMN),
            ]
        ),

        dcc.Graph(id='latestLocationPebble', figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}, style=COLUMNFULL),
        
        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="txnFees", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN),
                dbc.Col(dcc.Graph(id="txnFeesOut", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN)
            ]
        ),
    ]
)

# Scorecards
@app.callback(
    Output('deviceData', 'data'),
    [Input('dropdown', 'value')])
def update_output(value):
    deviceData = getDeviceData(value)
    return deviceData.to_json(date_format='iso', orient='split')

@app.callback(
    Output("timeLatestPebble", component_property='children'), 
    Input('dropdown', 'value'),
    Input('deviceData', 'data'))
def update_line_chart(value, data):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "Last Update Time: {}".format(filtered_df.iloc[0]["Last Data"])

@app.callback(
    Output("idLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "ID: {}".format(filtered_df.iloc[0]["Id"])

@app.callback(
    Output("nameLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "Name: {}".format(filtered_df.iloc[0]["Name"])

@app.callback(
    Output("addressLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "Address: {}".format(filtered_df.iloc[0]["Address"])

@app.callback(
    Output("ownerLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "Owner: {}".format(filtered_df.iloc[0]["Owner"])
