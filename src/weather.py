import requests
from dotenv import load_dotenv
import os

load_dotenv()


class Weather:

    def __init__(self):

        self.OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        self.API_KEY = os.environ["WEATHER_APIKEY"]
        self.account_sid = os.environ["WEATHER_ACCOUNT_SID"]
        self.auth_token = os.environ["WEATHER_AUTH_TOKEN"]
        self.city = "Granada"
        self.data = self.get_data_json()
        self.max_temp, self.min_temp = self.get_temps()
        self.rain = self.is_gonna_rain()

    def get_data_json(self):
        parameters = {
            "lat": os.getenv('WEATHER_LAT'),
            "lon": os.getenv('WEATHER_LON'),
            "cnt": 8,
            "appid": self.API_KEY,

        }

        response = requests.get(self.OWM_Endpoint, params=parameters)
        response.raise_for_status()
        data = response.json()
        return data

    def get_temps(self):
        max_temp = 0
        min_temp = 400
        for hours in self.data["list"]:
            if hours["main"]["temp_max"] > max_temp:
                max_temp = hours["main"]["temp_max"]
            if hours["main"]["temp_min"] < min_temp:
                min_temp = hours["main"]["temp_min"]

        max_temp = round((max_temp - 273.15), 2)
        min_temp = round((min_temp - 273.15), 2)
        return max_temp, min_temp

    def is_gonna_rain(self):
        gonna_rain = False
        for f in self.data["list"]:
            if f["weather"][0]["id"] < 701:
                gonna_rain = True

        return gonna_rain
