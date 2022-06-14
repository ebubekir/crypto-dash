import dash_bootstrap_components as dbc
from dash import html, dcc

from .callbacks import get_list_pair_options
import components

layout = html.Div(
    [
        dbc.Row([
            dcc.Loading([
                components.Box([
                    html.Div([
                        dcc.Interval(
                            id="crypto-overview-interval",
                            interval=1 * 1000,
                            n_intervals=0,
                            max_intervals=1,
                        )
                    ], id="crypto-overview-container", className="p-1 rounded-xl space-y-4"),
                ], title="Overview"),
            ]
            ),
        ]),
        dbc.Row([
            components.Box([
                "Box component test."
            ])
        ], style={"marginTop": "20px"})
    ])
