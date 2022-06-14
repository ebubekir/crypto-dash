from dash import html
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        html.H1('Prices Page', id="prices-page-output"),
        html.Button("Click me!", id="prices-page-click-btn")

    ])
