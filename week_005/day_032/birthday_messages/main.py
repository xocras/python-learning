# Extra Hard Starting Project
import pandas

from smtplib import SMTP
from random import randint
from datetime import datetime

YOU = "Oscar"
EMAIL_FROM = "-"
PASSWORD = "-"

# 1. Check if today matches a birthday in the birthdays.csv
today = datetime.now()

birthdays = pandas.read_csv("birthdays.csv").to_dict(orient="records")

birthdays = [
    birthday for birthday in birthdays
    if birthday['month'] == today.month and birthday['day'] == today.day
]

# 2. If step 2 is true, pick a random letter from letter templates
#    and replace the [NAME] with the person's actual name from birthdays.csv

with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
    starting_letter = file.read()

letters = {
    birthday['name']: {
        'letter': starting_letter.replace("[NAME]", birthday['name']).replace("[YOU]", YOU),
        'email': birthday['email']
    } for birthday in birthdays}

# 3. Send the letter generated in step 3 to that person's email address.

for name, item in letters.items():
    message = f"Subject:Happy Birthday {name}!\n\n{item['letter']}"
    email = item['email']

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(EMAIL_FROM, PASSWORD)

        connection.sendmail(EMAIL_FROM, email, message)


