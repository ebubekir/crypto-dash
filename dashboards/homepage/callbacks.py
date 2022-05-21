from dash import html
from services import CoinService
from components import indicator
from core import app

from dash import Output
from dash_extensions.enrich import Trigger


@app.callback(
    Output("crypto-overview-container", "children"),
    Trigger("crypto-overview-interval", "n_intervals")
)
def load_crypto_overview():
    coin_service = CoinService()
    df = coin_service.list_pairs(limit=10)
    response = []
    for data in [df[:5], df[5:]]:
        response = response + [
            html.Div([
                indicator(
                    value=i['last'],
                    title=i['pair_name'],
                    percentage=float(i['change_percent_val']),
                    sub_value=i['change_val']
                ) for i in data.to_dict('records')
            ], className="flex")
        ]
    return response
