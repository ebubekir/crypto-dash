from .homepage import layout

import importlib
from core import app
from dash import html, dcc, Output, Input
from components import content_container, sidebar

app.layout = html.Div([dcc.Location(id="url"), sidebar, content_container])


# Main callback for render page contents.
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return layout
    else:
        module = importlib.import_module(f'dashboards{pathname.replace("/", ".")}')
        return module.layout
