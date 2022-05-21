import dash_bootstrap_components as dbc
from dash import html
from components import indicator

layout = html.Div(
    [
        html.Div([
            indicator(12, 'BTC/USD', 3.41),
            indicator(12, 'BTC/USD', -20.43),
            indicator(12, 'BTC/USD', 0),
            indicator(12, 'BTC/USD', 3.41),
        ], className="summary-container")

    ])
