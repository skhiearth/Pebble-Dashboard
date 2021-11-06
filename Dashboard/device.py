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
import datetime
from datetime import datetime
import dash_table

# Import styles
from .style import *

# ---COMPONENTS---
ids = timeDf.Id.unique()

device = html.Div(
    [
        dcc.Store(id='deviceData'),
        html.Div(id='in-load'),

        dbc.Row(children=[
            dbc.Col([
                html.H5("Select a device by IMEI"),
                dcc.Dropdown(
                    id='dropdown',
                    options=[
                        {'label': i, 'value': i} for i in ids
                    ], value=ids[0]
                ), 
            ], style = COLUMNGREEN2),
            dbc.Col([
                html.H6("Device Name", style=HEADER),
                html.H5(id='nameLatestPebble', style=GREYSUBHEADING),
                html.H5(id='idLatestPebble', style=GREYSUBHEADINGSMALL),
            ], style = COLUMN4),
        ]),
        

        dbc.Row(children=[
                dbc.Col([
                    html.H6("Device Address", style=HEADER),
                    html.Div(
                        [
                            html.P(),
                            html.H5(id='addressLatestPebble', style=GREYSUBHEADINGSMALL),
                        ], style=COLUMN3DIV
                    ),
                ], style=COLUMN3),

                dbc.Col([
                    html.H6("Device Owner", style=HEADER),
                    html.Div(
                        [
                            html.P(),
                            html.H5(id='ownerLatestPebble', style=GREYSUBHEADINGSMALL),
                        ], style=COLUMN3DIV
                    ),
                ], style=COLUMN3),

                dbc.Col([
                    html.H6("Last updated", style=HEADER),
                    html.Div(
                        [
                            html.P(),
                            html.H5(id='timeLatestPebble', style=GREYSUBHEADINGSMALL),
                        ], style=COLUMN3DIV
                    ),
                ], style=COLUMN3),
            ]
        ),

        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H6("Last Known Location", style=HEADER),
                    dcc.Graph(id='latestLocationPebble'),
                ], style=COLUMN3),
            ]
        ),

        html.P(),

        dbc.Row(children=[
            dbc.Col([
                html.H6("Signal-to-noise ratio", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='snr', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Battery Voltage", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='vbat', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Temperature", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='temperature', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),
            ]
        ),

        dbc.Row(children=[
            dbc.Col([
                html.H6("Gas Resistance", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='gasResistance', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Pressure", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='pressure', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Humidity", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='humidity', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),
        ]),

        dbc.Row(children=[
            dbc.Col([
                html.H6("Ambient Light", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='light', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Gyroscope", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='gyroscope', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),

            dbc.Col([
                html.H6("Accelerometer", style=HEADER),
                html.Div(
                    [
                        html.P(),
                        html.H6(id='accelerometer', style=GREYSUBHEADING),
                    ], style=COLUMN3DIV
                ),
            ], style=COLUMN3),
        ]),

        html.P(),

        dbc.Row(children=[
                dbc.Col([
                    html.H6("Historic Data Points", style=HEADER),
                    html.Div(id='tableDiv'),
                ], style=COLUMN3),
            ]
        ),
        
        html.P(),
        html.Hr(),
        html.H6("Analytics of historic data sent by this pebble device"),
        html.P(),

        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="snrhist", style=GRAPHS,  figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN),
                dbc.Col(dcc.Graph(id="vbathist", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN)
            ]
        ),

        dbc.Row(children=[
                dbc.Col([
                    html.H6("Temperature and location over time", style=HEADER),
                    dcc.Graph(id='temperaturehistmap'),
                ], style=COLUMN3),
            ]
        ),

        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="temperaturehist", style=GRAPHS,  figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN),
                dbc.Col(dcc.Graph(id="temperature2hist", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN)
            ]
        ),

        dbc.Row(children=[
                dbc.Col([
                    html.H6("Pressure and location over time", style=HEADER),
                    dcc.Graph(id='pressurehistmap'),
                ], style=COLUMN3),
            ]
        ),

        # dcc.Graph(id='humidityhistmap', figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}, config={'displayModeBar': False}, style=COLUMNFULL),

        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="pressurehist", style=GRAPHS,  figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN),
                dbc.Col(dcc.Graph(id="humidityhist", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN)
            ]
        ),

        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="lighthist", style=GRAPHS,  figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN),
                dbc.Col(dcc.Graph(id="gasResistancehist", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#43C9BA', plot_bgcolor='#43C9BA')}, config={'displayModeBar': False}), style=COLUMNGREEN)
            ]
        ),

    ]
)

# Table
@app.callback(
    Output("tableDiv", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    data = data[["Timestamp", "Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", "Pressure", "Humidity", "Light"]]
    
    fig = dash_table.DataTable(
        id='users',
        columns=[{"name": i, "id": i} for i in data.columns],
        data=data.to_dict('records'),
        page_current= 0,
        page_size= 10,
        editable=True,
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'Snr',
                    'filter_query': '{Snr} lt 12'
                },
                'backgroundColor': 'red',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'Snr',
                    'filter_query': '{Snr} gt 30'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'Vbat',
                    'filter_query': '{Vbat} gt 4'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'Vbat',
                    'filter_query': '{Vbat} lt 3'
                },
                'backgroundColor': 'red',
                'color': 'white',
            },
        ]
    )
    return fig

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
    return "{}".format(filtered_df.iloc[0]["Last Data"])

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
    return "{}".format(filtered_df.iloc[0]["Name"])

@app.callback(
    Output("addressLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "{}".format(filtered_df.iloc[0]["Address"][0:8] + "..." + filtered_df.iloc[0]["Address"][-8:])

@app.callback(
    Output("ownerLatestPebble", component_property='children'), 
    [Input('dropdown', 'value')])
def update_line_chart(value):
    filtered_df = timeDf[timeDf['Id'] == value]
    return "{}".format(filtered_df.iloc[0]["Owner"][0:8] + "..." + filtered_df.iloc[0]["Owner"][-8:])

@app.callback(
    Output("snr", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{}".format(data.iloc[0]["Snr"])

@app.callback(
    Output("vbat", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{}V".format(data.iloc[0]["Vbat"])

@app.callback(
    Output("latitude", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{}".format(data.iloc[0]["Latitude"])

@app.callback(
    Output("longitude", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{}".format(data.iloc[0]["Longitude"])

@app.callback(
    Output("gasResistance", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{}".format(data.iloc[0]["Gas Resistance"])

@app.callback(
    Output("temperature", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{} deg C".format(data.iloc[0]["Temperature"])

@app.callback(
    Output("pressure", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{} hPa".format(data.iloc[0]["Pressure"])

@app.callback(
    Output("humidity", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "Humidity: {}".format(data.iloc[0]["Humidity"])

@app.callback(
    Output("light", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{} lux".format(data.iloc[0]["Light"])

@app.callback(
    Output("temperature2", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "{} deg C".format(data.iloc[0]["Temperature2"])

@app.callback(
    Output("gyroscope", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "X: {}, Y: {}, Z: {}".format(data.iloc[0]["Gyroscope1"], data.iloc[0]["Gyroscope2"], data.iloc[0]["Gyroscope3"])

@app.callback(
    Output("accelerometer", component_property='children'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    
    return "X: {}, Y: {}, Z: {}".format(data.iloc[0]["Accelerometer1"], data.iloc[0]["Accelerometer2"], data.iloc[0]["Accelerometer3"])

# Map
@app.callback(
    Output("latestLocationPebble", component_property='figure'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    data = data.head(1)
    
    fig = px.scatter_geo(data,
                    lat=data["Latitude"],
                    lon=data["Longitude"],
                    hover_data=["Snr", "Vbat", "Latitude", "Longitude", "Gas Resistance", "Temperature", "Pressure", "Humidity", "Light"],
                    hover_name="Timestamp")
    fig.update_geos(projection_type="natural earth")

    return fig

@app.callback(
    Output("temperaturehistmap", component_property='figure'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    fig = px.scatter_geo(data,
                    lat=data["Latitude"],
                    lon=data["Longitude"],
                    size="Temperature",
                    animation_frame=data.Timestamp.astype(str))
    return fig

@app.callback(
    Output("humidityhistmap", component_property='figure'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    fig = px.scatter_geo(data,
                    lat=data["Latitude"],
                    lon=data["Longitude"],
                    title="Humidity and location over time (hover over to see humidity at the time)",
                    size="Humidity",
                    animation_frame=data.Timestamp.astype(str), template='plotly_dark').update_layout(
        {'plot_bgcolor': '#262525', 'paper_bgcolor': '#262525', 'dragmode': False})
    return fig

@app.callback(
    Output("pressurehistmap", component_property='figure'), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')
    fig = px.scatter_geo(data,
                    lat=data["Latitude"],
                    lon=data["Longitude"],
                    size="Pressure",
                    animation_frame=data.Timestamp.astype(str))
    return fig

# Historic
@app.callback(
    Output("snrhist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Signal-to-noise ratio <br>Latest on {}: {}".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Snr"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Snr", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("vbathist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Battery Voltage <br>Latest on {}: {}V".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Vbat"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Vbat", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("temperaturehist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Temperature (Motion Sensor) <br>Latest on {}: {} deg C".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Temperature2"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Temperature2", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("temperature2hist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Temperature <br>Latest on {}: {} deg C".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Temperature"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Temperature", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("gasResistancehist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Gas Resistance <br>Latest on {}: {} ".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Gas Resistance"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Gas Resistance", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("pressurehist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Pressure <br>Latest on {}: {} hPa".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Pressure"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Pressure", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("humidityhist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Humidity <br>Latest on {}: {}".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Humidity"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Humidity", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig

@app.callback(
    Output("lighthist", "figure"), 
    Input('deviceData', 'data'))
def update_line_chart(data):
    data = pd.read_json(data, orient='split')

    titletext = "Light <br>Latest on {}: {} lux".format(data["Timestamp"].iat[0].strftime("%d-%m-%Y"),
    str(data["Light"].iat[0]))
    fig = px.line(data, 
        x="Timestamp", y="Light", 
        title=titletext
        )
    fig.update_layout({
        "plot_bgcolor": "#43C9BA",
        "paper_bgcolor": "#43C9BA",
    })
    if(data.shape[0] > 40):
        fig.update_layout(xaxis_range=[data["Timestamp"].iat[40], data["Timestamp"].iat[0]])
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(step="all")
                ])
            )
    )
    fig['data'][0]['line']['color']="#21625B"
    return fig