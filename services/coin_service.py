import pandas as pd
from typing import List

from .api_service import ApiService


class CoinService(ApiService):
    def list_pairs(self, limit: int = 8):
        querystring = {"time_utc_offset": "28800", "lang_ID": "1"}
        response = self.get(url="coins/list-pairs", params=querystring)
        df = pd.DataFrame([s['screen_data']['pairs_data'] for s in response][0])
        df = df.head(limit)
        df = df[['last', 'change_percent_val', 'change_val', 'pair_name']]
        return df
