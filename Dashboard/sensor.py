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
from datetime import datetime, date

# Import styles
from .style import *

# ---COMPONENTS---
ids = timeDf.Owner.unique()

# Load the dataset
sensor = html.Div(
    [
        dcc.Store(id='intermediate-value-in-00'),
        dbc.Row(dbc.Col(html.Div(html.H3("Sensor Analytics", style=HEADING)))),
        html.H5("Intelligent insights derived from current data to get sense of current health of devices"),
        dcc.Store(id='sensorData'),
        html.Div(id='in-load-sensor'),

        html.P(),
        html.P(),

        html.H6("Filter by date range: "),

        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=date(2021, 9, 1),
            max_date_allowed=date.today(),
            initial_visible_month=date.today(),
            end_date=date.today()
        ),
        html.Div(id='output-container-date-picker-range'),


        html.P(),
        html.P(),
        html.P(),
        html.P(),

        html.H6("Filter by device owner: "),

        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': i, 'value': i} for i in ids
            ], value=""
        ),

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

        html.Hr(),
        html.H4("Temperature"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="tempmin")),
                    html.H5(html.Center("deg C")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="tempmax")),
                    html.H5(html.Center("deg C")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="tempmean")),
                    html.H5(html.Center("deg C")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="tempmedian")),
                    html.H5(html.Center("deg C")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="tempmode")),
                    html.H5(html.Center("deg C")),
                ], style=COLUMN),
            ]
        ),

        html.Hr(),
        html.H4("Pressure"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="premin")),
                    html.H5(html.Center("hPa")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="premax")),
                    html.H5(html.Center("hPa")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="premean")),
                    html.H5(html.Center("hPa")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="premedian")),
                    html.H5(html.Center("hPa")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="premode")),
                    html.H5(html.Center("hPa")),
                ], style=COLUMN),
            ]
        ),


        html.Hr(),
        html.H4("Gas Resistance"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="gasmin")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="gasmax")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="gasmean")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="gasmedian")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="gasmode")),
                ], style=COLUMN),
            ]
        ),

        html.Hr(),
        html.H4("Humidity"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="hummin")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="hummax")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="hummean")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="hummedian")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="hummode")),
                ], style=COLUMN),
            ]
        ),


        html.Hr(),
        html.H4("Light"),
        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H5(html.Center("Minimum")),
                    html.Center(html.H1(id="limin")),
                    html.H5(html.Center("lux")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Maximum")),
                    html.Center(html.H1(id="limax")),
                    html.H5(html.Center("lux")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mean")),
                    html.Center(html.H1(id="limean")),
                    html.H5(html.Center("lux")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Median")),
                    html.Center(html.H1(id="limedian")),
                    html.H5(html.Center("lux")),
                ], style=COLUMN),
                dbc.Col([
                    html.H5(html.Center("Mode")),
                    html.Center(html.H1(id="limode")),
                    html.H5(html.Center("lux")),
                ], style=COLUMN),
            ]
        ),
    ]

    
)

@app.callback(
    Output('output-container-date-picker-range', 'children'),
    Output('intermediate-value-in-00', 'data'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '

    start_date_object = date(2021, 1, 1)
    end_date_object = date.today()

    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%B %d, %Y')
        string_prefix = string_prefix + 'End Date: ' + end_date_string

    sensorDf = timeDf[(timeDf['Date']>=start_date_object) & (timeDf['Date']<=end_date_object)]  

    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here', sensorDf.to_json(date_format='iso', orient='split')
    else:
        return string_prefix, sensorDf.to_json(date_format='iso', orient='split')

@app.callback(
    Output("snrmin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Snr"].min())

@app.callback(
    Output("snrmax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Snr"].max())

@app.callback(
    Output("snrmean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Snr"].mean(), 2))

@app.callback(
    Output("snrmedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Snr"].median(), 2))

@app.callback(
    Output("snrmode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Snr"].mode()[0])

@app.callback(
    Output("vbatmin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Vbat"].min())

@app.callback(
    Output("vbatmax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Vbat"].max())

@app.callback(
    Output("vbatmean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Vbat"].mean(), 2))

@app.callback(
    Output("vbatmedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Vbat"].median(), 2))

@app.callback(
    Output("vbatmode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Vbat"].mode()[0])

# Temperature
@app.callback(
    Output("tempmin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Temperature"].min())

@app.callback(
    Output("tempmax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Temperature"].max())

@app.callback(
    Output("tempmean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Temperature"].mean(), 2))

@app.callback(
    Output("tempmedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Temperature"].median(), 2))

@app.callback(
    Output("tempmode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Temperature"].mode()[0])


# Pressure
@app.callback(
    Output("premin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Pressure"].min())

@app.callback(
    Output("premax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Pressure"].max())

@app.callback(
    Output("premean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Pressure"].mean(), 2))

@app.callback(
    Output("premedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Pressure"].median(), 2))

@app.callback(
    Output("premode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Pressure"].mode()[0])


# Gas Resistance
@app.callback(
    Output("gasmin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Gas Resistance"].min())

@app.callback(
    Output("gasmax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Gas Resistance"].max())

@app.callback(
    Output("gasmean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Gas Resistance"].mean(), 2))

@app.callback(
    Output("gasmedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Gas Resistance"].median(), 2))

@app.callback(
    Output("gasmode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Gas Resistance"].mode()[0])


# Humidity
@app.callback(
    Output("hummin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Humidity"].min())

@app.callback(
    Output("hummax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Humidity"].max())

@app.callback(
    Output("hummean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Humidity"].mean(), 2))

@app.callback(
    Output("hummedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Humidity"].median(), 2))

@app.callback(
    Output("hummode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Humidity"].mode()[0])


# Light
@app.callback(
    Output("limin", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Light"].min())

@app.callback(
    Output("limax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Light"].max())

@app.callback(
    Output("limean", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Light"].mean(), 2))

@app.callback(
    Output("limedian", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Light"].median(), 2))

@app.callback(
    Output("limode", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(sensorDf["Light"].mode()[0])