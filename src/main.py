from weather import Weather
from google_data import GoogleData
from mail_system import MailSystem
import random


with open(file="../data/quote_data.csv", mode="r") as file:
    quote_list = file.readlines()

wh = Weather()
gd = GoogleData()
ms = MailSystem(subject=f"Planing {gd.formatted_date}", body=f"Good morning!\n"
                                                             f"It is 9 o'clock in the morning on {gd.formatted_date}.\n"
                                                             f"The minimum temperature is {wh.min_temp}ºC "
                                                             f"and the maximum is {wh.max_temp}ºC\n"
                                                             f"The task(s) of the day:\n"
                                                             f"{gd.activity}\n\n"
                                                             f"Lunch: {gd.lunch}\n"
                                                             f"Dinner: {gd.dinner}\n"
                                                             f"Have a great day!\n\n"
                                                             f"{random.choice(quote_list)}")
print(ms.send_email())

