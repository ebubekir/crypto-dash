import dash_bootstrap_components as dbc
from dash import html, dcc
from components import indicator
from .callbacks import load_crypto_overview

layout = html.Div(
    [
        dcc.Loading([
            html.H1("Overview", className="text-2xl font-medium "),
            html.Div([
                dcc.Interval(
                    id="crypto-overview-interval",
                    interval=1 * 1000,
                    n_intervals=0,
                    max_intervals=1,
                )
            ], id="crypto-overview-container", className="  border-2 border-gray-300 p-1 rounded-xl space-y-4"),

        ]

        )
    ])
