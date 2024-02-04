from smtplib import SMTP
from random import choice
from datetime import datetime

EMAIL_FROM = "-"
EMAIL_TO = "-"
PASSWORD = "-"

MONDAY = 0


def send_message():
    with open("quotes.txt") as file:
        quote = choice([line.strip() for line in file.readlines()])

    message = f"Subject:Weekly Motivation\n\n{quote}"

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(EMAIL_FROM, PASSWORD)

        connection.sendmail(EMAIL_FROM, EMAIL_TO, message)


if datetime.now().weekday() == MONDAY:
    send_message()
    print("Sent!")
