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
        dcc.Store(id='sensorData'),
        html.Div(id='in-load-sensor'),

        html.P(),

        dbc.Row(children=[
            dbc.Col([
                html.H6("Filter by device owner: ", style=HEADER),
                dcc.Dropdown(
                    id='dropdown',
                    options=[
                        {'label': i, 'value': i} for i in ids
                    ], value=""
                ),
            ], style = COLUMNGREEN),
            dbc.Col([
                html.H5("Filter by date range: ", style=HEADER),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=date(2021, 9, 1),
                    max_date_allowed=date.today(),
                    initial_visible_month=date.today(),
                    end_date=date.today()
                ),
                html.Div(id='output-container-date-picker-range'),
            ], style = COLUMNGREEN),
        ]),

        html.P(),
        html.P(),
        html.H4("Signal-to-noise ratio", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="snrmin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="snrmax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="snrmean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="snrmedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="snrmode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Battery Voltage", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="vbatmin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Volts")),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="vbatmax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Volts")),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="vbatmean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Volts")),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="vbatmedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Volts")),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="vbatmode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Volts")),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Temperature", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="tempmin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("deg C")),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="tempmax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("deg C")),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="tempmean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("deg C")),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="tempmedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("deg C")),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="tempmode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("deg C")),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Pressure", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="premin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("hPa")),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="premax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("hPa")),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="premean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("hPa")),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="premedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("hPa")),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="premode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("hPa")),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Gas Resistance", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="gasmin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="gasmax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="gasmean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="gasmedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="gasmode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Humidity", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="hummin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="hummax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="hummean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="hummedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="hummode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
            ]
        ),

        html.P(),
        html.P(),
        html.H4("Light", style=HEADER),

        dbc.Row(children=[
                dbc.Col([
                    html.Center(html.H1(id="limin", style=GREYSUBHEADING2)),
                    html.H5(html.Center("lux")),
                    html.H5(html.Center("Minimum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="limax", style=GREYSUBHEADING2)),
                    html.H5(html.Center("lux")),
                    html.H5(html.Center("Maximum", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="limean", style=GREYSUBHEADING2)),
                    html.H5(html.Center("lux")),
                    html.H5(html.Center("Mean", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="limedian", style=GREYSUBHEADING2)),
                    html.H5(html.Center("lux")),
                    html.H5(html.Center("Median", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
                dbc.Col([
                    html.Center(html.H1(id="limode", style=GREYSUBHEADING2)),
                    html.H5(html.Center("lux")),
                    html.H5(html.Center("Mode", style=GREENHEADINGSMALL2)),
                ], style=COLUMN3),
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
    return "{}".format(round(sensorDf["Light"].min(), 2))

@app.callback(
    Output("limax", component_property='children'), 
    Input('intermediate-value-in-00', 'data'), Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'), Input('dropdown', 'value'))
def update_line_chart(data, start_date, end_date, value):
    sensorDf = pd.read_json(data, orient='split')
    if(value != ""):
        sensorDf = sensorDf[sensorDf["Owner"] == value]
    return "{}".format(round(sensorDf["Light"].max(), 2))

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
    return "{}".format(round(sensorDf["Light"].mode()[0], 2))