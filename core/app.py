from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP,
                          "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"],
    external_scripts=["https://cdn.tailwindcss.com"],
    suppress_callback_exceptions=True
)
