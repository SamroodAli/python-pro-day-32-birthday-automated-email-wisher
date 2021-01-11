import pandas
import datetime as dt
import random

contacts = pandas.read_csv("birthdays.csv").to_dict(orient="records")

now = dt.datetime.now()
for contact in contacts:
    print(contact)
    if contact["month"] == now.month and contact["day"] == now.day:
       print("contact access correct")
