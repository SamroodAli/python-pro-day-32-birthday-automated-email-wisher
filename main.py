import pandas
import datetime as dt
import random

contacts = pandas.read_csv("birthdays.csv").to_dict(orient="records")

now = dt.datetime.now()
for contact in contacts:
    template = random.randint(1, 3)
    if contact["month"] == now.month and contact["day"] == now.day:
        with open(f"letter_templates/letter_{template}.txt") as template:
            sample_template = template.read()