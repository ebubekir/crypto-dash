from dash import html
from services import CoinService
from components import indicator

from core import app
from core import cache

from dash import Output, Input
import plotly.graph_objects as go
from dash_extensions.enrich import Trigger


@cache.memoize(expire=3600)
def get_list_pair_options():
    cs = CoinService()
    return cs.list_pairs_options()


@app.callback(
    Output("crypto-overview-container", "children"),
    Trigger("crypto-overview-interval", "n_intervals")
)
@cache.memoize(expire=3600)
def load_crypto_overview():
    coin_service = CoinService()
    df = coin_service.overview_metrics(limit=10)
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


@app.callback(
    Input("homepage-pairs-options", "value"),
    Output("pair-historical-data-graph", "figure")
)
@cache.memoize(expire=3600)
def get_historical_pair_graph(pair_id):
    coin_service = CoinService()
    df = coin_service.get_historical_data(pair_id=pair_id)
    fig = go.Figure(
        [
            go.Scatter(x=df['date'],
                       y=df['price'],
                       name="Price",
                       hovertemplate="Date: %{x} <br>Price: %{y} <br>Change: %{customdata}",
                       customdata=df['perc_chg'],
                       ),
            go.Scatter(x=df['date'],
                       y=df['low'],
                       name="Low",
                       hovertemplate="Date: %{x} <br>Price: %{y} <br>Change: %{customdata}",
                       customdata=df['perc_chg']
                       ),
            go.Scatter(x=df['date'],
                       y=df['high'],
                       name="High",
                       hovertemplate="Date: %{x} <br>Price: %{y} <br>Change: %{customdata}",
                       customdata=df['perc_chg'],
                       )
        ]
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", )

    return fig
