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
overview = html.Div(
    [
        dbc.Row([
            dcc.Store(id='intermediate-value-in-0'),
            dcc.Store(id='intermediate-value-in-00'),
            dcc.Store(id='intermediate-value-in-000'),
            dcc.Store(id='intermediate-value-in-0000'),
            html.Div(id='in-load'),
            dbc.Col(html.Div(html.H3("Overview", style=HEADING))),
        ]),
        dbc.Row([
            html.H5("Compare with:", style=TEXT),
            dcc.Checklist(
                id="checklist",
                options=[{"label": x, "value": x} 
                        for x in networks],
                value=networks[0:1],
                labelStyle={'display': 'inline-block', 'margin': '5px', 'padding': '3px', "font-family": 'DM Mono, monospace',}
            )
        ], style={'margin-left': '10px'}),
        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="allTxns", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN),
                dbc.Col(dcc.Graph(id="uniqueAddresses", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN)
            ]
        ),
        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="cummulativeNetworkFee", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN),
            ]
        ),
        dbc.Row(children=[
                dbc.Col(dcc.Graph(id="networkStats1", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN),
                dbc.Col(dcc.Graph(id="networkStats2", style=GRAPHS, figure={'layout': go.Layout(paper_bgcolor='#262525', plot_bgcolor='#262525')}), style=COLUMN)
            ]
        ),
    ]
)

# Load data
@app.callback(
    Output('intermediate-value-in-0', 'data'),
    [dash.dependencies.Input('in-load', 'n_clicks')])
def update_output(n_clicks):
    txnsByDate = pd.read_csv('https://storage.googleapis.com/iotube/txnStats')
    return txnsByDate.to_json(date_format='iso', orient='split')

@app.callback(
    Output('intermediate-value-in-00', 'data'),
    [dash.dependencies.Input('in-load', 'n_clicks')])
def update_output(n_clicks):
    networkStats = pd.read_csv('https://storage.googleapis.com/iotube/networkStatsNew')
    return networkStats.to_json(date_format='iso', orient='split')

@app.callback(
    Output('intermediate-value-in-000', 'data'),
    [dash.dependencies.Input('in-load', 'n_clicks')])
def update_output(n_clicks):
    df = pd.read_csv('https://storage.googleapis.com/iotube/yearHourData')
    return df.to_json(date_format='iso', orient='split')

@app.callback(
    Output('intermediate-value-in-0000', 'data'),
    [dash.dependencies.Input('in-load', 'n_clicks')])
def update_output(n_clicks):
    df = pd.read_csv('https://storage.googleapis.com/iotube/newHourData')
    return df.to_json(date_format='iso', orient='split')
    
# Daily Transactions
@app.callback(
    Output("allTxns", "figure"), 
    Input(component_id='checklist', component_property='value'),
    Input('intermediate-value-in-0', 'data'))
def update_line_chart(value, data):
    txnsByDate = pd.read_json(data, orient='split')
    mask = txnsByDate.Network.isin(value)
    fig = px.line(txnsByDate[mask], 
        x="Date", y="Transactions", color="Network", color_discrete_sequence=["#38FF99", "#8147E5", "red", "goldenrod", "magenta"],
        title="Daily Transactions", template='plotly_dark').update_layout(
        {'plot_bgcolor': '#262525', 'paper_bgcolor': '#262525'})
    return fig