from core import app
from dash import Output
from dash_extensions.enrich import Trigger


@app.callback(
    Output("test-output", "children"),
    Trigger("click-btn", "n_clicks"),
    prevent_initial_call=True
)
def test_callback(a):
    return "Clicked!"
