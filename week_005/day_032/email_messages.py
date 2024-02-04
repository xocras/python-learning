from smtplib import SMTP

# SMTP: Simple Mail Transfer Protocol

# TLS: Transport Layer Security

EMAIL = "-"
PASSWORD = "-"
MESSAGE = "Subject:Hello World!\n\nThis is an instant message from Python."

with SMTP("smtp.gmail.com") as connection:

    connection.starttls()

    connection.login(EMAIL, PASSWORD)

    connection.sendmail(EMAIL, EMAIL, MESSAGE)


