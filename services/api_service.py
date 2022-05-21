import json
import traceback
import requests
from core import settings


class ApiService:
    def __init__(self):
        self.api_url = "https://investing-cryptocurrency-markets.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Host": settings.API_HOST,
            "X-RapidAPI-Key": settings.API_KEY
        }

    def get(self, url, **kwargs):
        try:
            response = requests.request("GET", self.api_url + url, headers=self.headers, **kwargs)
            if response.status_code != 200:
                raise Exception(f"An error occurred with Investing API Connection Details: {response.text}")
            return json.loads(response.text)['data']
        except Exception as e:
            traceback.print_exc()
            raise e
