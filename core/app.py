from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
