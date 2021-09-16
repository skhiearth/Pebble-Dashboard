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
IOTUBE_LOGO = "https://app.iott.network/images/logo.png"
MISFITS_LOGO = "https://raw.githubusercontent.com/skhiearth/VacSeen/main/UI%20Elements/misfits_logo.png"

navbar = dbc.Navbar([
    html.A(
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                dbc.Col(html.Img(src=IOTUBE_LOGO, height="30px")),
                dbc.Col(dbc.NavbarBrand("Pebble Analytics", className="ml-2")),
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
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

footer = dbc.Navbar([
    html.A(
        # Use row and col to control vertical alignment of logo / brand
        dbc.Row(
            [
                dbc.Col(html.Img(src=MISFITS_LOGO, height="30px")),
                dbc.Col(dbc.NavbarBrand("Made by The Misfits for Grants Round 11 Hackathon by Gitcoin and IoTeX", className="ml-3")),
            ],
            align="center",
            no_gutters=True,
        ), 
        href="http://themisfits.xyz/",
    ),
], color="#3B3B3B", dark=True, style=FOOTER_STYLE)

content = html.Div(id="page-content", style=CONTENT_STYLE)