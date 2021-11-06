# Import libraries
from .server import app
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Import styles
from .style import *

# ---COMPONENTS---
MISFITS_LOGO = "https://raw.githubusercontent.com/skhiearth/VacSeen/main/UI%20Elements/misfits_logo.png"

navbar = dbc.Navbar([
    html.A(
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                dbc.Col(html.Img(src='https://raw.githubusercontent.com/skhiearth/Pebble-Dashboard/main/assets/satwhite.png', height="30px")),
                dbc.Col(dbc.NavbarBrand("TruStream Dashboard", className="ml-2")),
            ],
            align="center",
            no_gutters=True,
        ), 
        href="/",
    ),
    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
], color="#3B3B3B", dark=True, style=NAVBAR_STYLE, sticky="top")

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact", style=NAVLINK),
                dbc.NavLink("Devices", href="/device", active="exact", style=NAVLINK),
                dbc.NavLink("Sensor Analytics", href="/sensor", active="exact", style=NAVLINK),
                dbc.NavLink("About TruStream",  target="_blank", href="https://iotex.gitbook.io/trustream", active="exact", style=NAVLINK),
            ],
            vertical=True,
            pills=True,
        ),

        html.Hr(),
        html.P(),
        html.P(),

        dbc.Row([
                dbc.Col(html.H6("Made by The Misfits")),
            ],
            align="center",
            no_gutters=True, style=ROWW
        ), 

        html.A("skhiearth", href="https://skhiearth.xyz", target="_blank", style=ROWW),
        html.A("⚡", style=ROWW),
        html.A("simmsss", href="https://simmsss.github.io", target="_blank", style=ROWW),

        dbc.Row(
            [
                dbc.Col(html.H6("for Grants Round 11 Hackathon by Gitcoin and IoTeX")),
            ],
            align="center",
            no_gutters=True,
        ), 

    ],
    style=SIDEBAR_STYLE
)

content = html.Div(id="page-content", style=CONTENT_STYLE)