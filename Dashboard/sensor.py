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

# Import styles
from .style import *

# ---COMPONENTS---

# Load the dataset
sensor = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(html.H3("Sensor Analytics", style=HEADING)))),
        dcc.Store(id='sensorData'),
        html.Div(id='in-load-sensor'),
    ]
)