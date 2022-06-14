from datetime import datetime

import pandas as pd

from .api_service import ApiService


class CoinService(ApiService):
    def list_pairs(self) -> pd.DataFrame:
        querystring = {"time_utc_offset": "28800", "lang_ID": "1"}
        response = self.get(url="coins/list-pairs", params=querystring)
        df = pd.DataFrame([s['screen_data']['pairs_data'] for s in response][0])
        return df

    def overview_metrics(self, limit: int = 8) -> pd.DataFrame:
        df = self.list_pairs()
        df = df.head(limit)
        df = df[['last', 'change_percent_val', 'change_val', 'pair_name']]
        return df

    def list_pairs_options(self) -> list:
        df = self.list_pairs()
        df = df[['pair_ID', 'pair_name']]
        return df.eval(
            """
                label=pair_name
                value=pair_ID
            """
        )[['label', 'value']].to_dict('records')

    def get_historical_data(self, pair_id: str) -> pd.DataFrame:
        querystring = {"pair_ID": pair_id, "date_from": "20012020", "date_to": "19022020", "lang_ID": "1",
                       "time_utc_offset": "28800", "interval": "day"}
        response = self.get(url="coins/get-historical-data", params=querystring)
        df = pd.DataFrame(response[0]['screen_data']['data'])
        df['date'] = df['date'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d'))
        df['price'] = df['price'].apply(lambda x: float(x.replace(',', '')))
        return df
