import pandas as pd
from typing import List

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
