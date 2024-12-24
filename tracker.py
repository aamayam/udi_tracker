import pandas as pd
import requests
from datetime import datetime as dt

class UDITracker:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://www.banxico.org.mx/SieAPIRest/service/v1/"
        self.headers = {
            "Bmx-token": token,
            "Accept": "application/json"
        }

    def get_udi_series(self, time_start, time_end=None):
        if time_end == None:
            time_end = dt.now().strftime('%Y-%m-%d')

        url = f"{self.base_url}/series/SP68257/datos/{time_start}/{time_end}"

        try:
            response = requests.get(url=url,headers=self.headers)
            response.raise_for_status()

            data = response.json()
            series = data['bmx']['series'][0]['datos']

            df = pd.DataFrame(series)
            df.columns = ['fecha', 'valor']
            df['valor'] = pd.to_numeric(df['valor'])
            df['fecha'] = pd.to_datetime(df['fecha'])

            return df
        except:
            print(f"Error while retrieving data")
            return None