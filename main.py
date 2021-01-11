import pandas
import datetime as dt
import random
import smtplib
from user_mail_data import EMAIL, PASSWORD

# placeholder to replace in template
TEMPLATE_PLACEHOLDER = "[NAME]"

# Reading csv contacts data, each contact as a record
contacts_records = pandas.read_csv("birthdays.csv").to_dict(orient="records")
# Sorting contacts records as (month,day): contact_record
contacts_birthdays = {
    (contact["month"], contact["day"]): contact
    for contact in contacts_records
}

# Getting today from datetime module
today = dt.datetime.now()
# Saving today's month and day
today_tuple = (today.month, today.day)

# If today is in birthday list
if today_tuple in contacts_birthdays:
    # getting birthday person
    birthday_person = contacts_birthdays[today_tuple]

    # Choosing a random template
    template = random.randint(1, 3)
    file_path = f"letter_templates/letter_{template}.txt"

    # Opening template and sending mail
    with open(file_path) as template:
        # reading template
        sample_template = template.read()
        # replacing placeholder
        mail_body = sample_template.replace(TEMPLATE_PLACEHOLDER, birthday_person["name"])
        # opening mail connection using smtp library
        # for gmail - smtp.gmail.com
        # for outlook - smtp.live.com
        # for yahoo - smtp.mail.yahoo.com
        with smtplib.SMTP("smtp.live.com") as connection:
            # boilerplate to securing our email communication, tls = Transport Layer Security
            connection.starttls()
            # Sender email address and password to login
            connection.login(user=EMAIL, password=PASSWORD)
            # Sending mail, from sender, to recipient,
            # and message body = "Subject:your subject here\n\n the content of the mail here"
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{mail_body}"
            )
