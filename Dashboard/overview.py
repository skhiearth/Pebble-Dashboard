# Import libraries
from datetime import time
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
import dash_table

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
                    html.H6("Device Stats"),
                    html.Hr(style=RULE),
                    html.P(),
                    html.H6(id='totalDevices'),
                    html.H6(id='confirmedDevices'),
                    html.H6(id='pendingDevices'),
                    html.H6(id='activeData'),
                    html.H6(id='noData'),
                ], style=COLUMN3),

                dbc.Col([
                    html.H6("Owner Stats"),
                    html.Hr(style=RULE),
                    html.P(),
                    html.H6(id='firstDevices'),
                    html.H6(id='secondDevices'),
                    html.H6(id='thirdDevices'),
                ], style=COLUMN3),

                dbc.Col([
                    html.H6("Last data from"),
                    html.Hr(style=RULE),
                    html.P(),
                    html.H6(id='timeLatest'),
                    html.H6(id='idLatest'),
                    html.H6(id='nameLatest'),
                    html.H6(id='addressLatest'),
                    html.H6(id='ownerLatest'),
                ], style=COLUMN3),
            ]
        ),

        html.Hr(),

        html.P(),

        dcc.Graph(id='latestLocation', figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}, style=COLUMNFULL),

        html.Hr(),

        html.P(),

        html.H4("Live Data Table"),
        html.H6("Data table showing the latest datapoints entering TruStream"),
        html.P(),

        dbc.Row(children=[
                dbc.Col(html.Div(id='liveTable'), style=COLUMNGREEN),
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

@app.callback(
    Output("piechart", component_property='figure'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    labels = ['Confirmed','Pending','Active','No Data']
    values = [len(statusDf[statusDf["Status"] == 2]), 
    len(statusDf[statusDf["Status"] == 1]), 
    len(statusDf[statusDf["Raw Data"] != "No Data"]), 
    len(statusDf[statusDf["Raw Data"] == "No Data"])]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout({
        "paper_bgcolor": "#262525",
        "showlegend": False
    })
    return fig


# Owner Frequency
@app.callback(
    Output("firstDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[0],
    statusDf.Owner.value_counts()[:4].index.tolist()[0][0:6] + "..." + statusDf.Owner.value_counts()[:4].index.tolist()[0][-6:])

@app.callback(
    Output("secondDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[1],
    statusDf.Owner.value_counts()[:4].index.tolist()[1][0:6] + "..." + statusDf.Owner.value_counts()[:4].index.tolist()[1][-6:])

@app.callback(
    Output("thirdDevices", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "{} devices: {}".format(statusDf.Owner.value_counts()[2],
    statusDf.Owner.value_counts()[:4].index.tolist()[2][0:6] + "..." + statusDf.Owner.value_counts()[:4].index.tolist()[2][-6:])


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
    return "Address: {}".format(timeDf.iloc[0]["Address"][0:6] + "..." + timeDf.iloc[0]["Address"][-6:])

@app.callback(
    Output("addressOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Address: {}".format(timeDf.iloc[-1]["Address"])

@app.callback(
    Output("ownerLatest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Owner: {}".format(timeDf.iloc[0]["Owner"][0:6] + "..." + timeDf.iloc[0]["Owner"][-6:])

@app.callback(
    Output("ownerOldest", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    return "Owner: {}".format(timeDf.iloc[-1]["Owner"])

# Map
@app.callback(
    Output("latestLocation", component_property='figure'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    fig = px.scatter_geo(timeDf,
                    lat=timeDf["Latitude"],
                    lon=timeDf["Longitude"],
                    hover_data=["Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", "Pressure", "Humidity", "Light"],
                    title="Latest location of Pebble Devices (hover over to see ID)",
                    hover_name="Id", template='plotly_dark').update_layout(
        {'plot_bgcolor': '#262525', 'paper_bgcolor': '#262525', 'dragmode': False})
    fig.update_geos(projection_type="natural earth")
    return fig

# Table
@app.callback(
    Output("liveTable", component_property='children'), 
    Input('statusData', 'data'))
def update_line_chart(data):
    data = timeDf[["Last Data", "Id", "Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", "Pressure", "Humidity", "Light"]]
    
    fig = dash_table.DataTable(
        id='users',
        columns=[{"name": i, "id": i} for i in data.columns],
        data=data.to_dict('records'),
        style_table={'overflowX': 'scroll'},
        page_current= 0,
        page_size= 10,
    )
    return fig