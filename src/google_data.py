from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class GoogleData:

    def __init__(self):
        self.sh_endpoint = os.environ["SHEETY_ENDPOINT"]
        self.date = datetime.now()
        self.formatted_date = self.date.strftime("%d/%m/%Y")
        self.google_data = self.get_google_data()
        self.row_day = self.get_day_data()
        self.activity = self.row_day["activity"]
        self.lunch = self.row_day["lunch"]
        self.dinner = self.row_day["dinner"]

    def get_google_data(self):
        response = requests.get(self.sh_endpoint)
        data = response.json()
        return data["days"]

    def get_day_data(self):
        date = self.formatted_date
        for row in self.google_data:
            if row["date"] == date:
                print(row)
                return row
