import pandas
import datetime as dt
import random
import smtplib
from user_mail_data import EMAIL, PASSWORD

TEMPLATE_PLACEHOLDER = "[NAME]"

contacts = pandas.read_csv("birthdays.csv").to_dict(orient="records")
today = dt.datetime.now()

for contact in contacts:
    template = random.randint(1, 3)
    if contact["month"] == today.month and contact["day"] == today.day:
        with open(f"letter_templates/letter_{template}.txt") as template:
            sample_template = template.read()
            mail_body = sample_template.replace(TEMPLATE_PLACEHOLDER,contact["name"])

            with smtplib.SMTP("smtp.live.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=contact["email"],
                    msg=f"Subject:Happy Birthday!\n\n{mail_body}"
                )
