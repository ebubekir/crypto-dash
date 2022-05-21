from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa"
}

sidebar = html.Div(
    [
        html.H2("Crypto Dash", className="display-4"),
        html.Hr(),
        html.P("A crypto dashboard built with Dash Plotly", className="lead"),
        dbc.Nav([
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Prices", href="/prices", active="exact")
        ], vertical=True, pills=True)
    ], style=SIDEBAR_STYLE
)

