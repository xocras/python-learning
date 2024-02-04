import requests

from twilio.rest import Client

# OpenWeatherMap
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "-"
LAT, LON = 0, 0

# Twilio
ACCOUNT_SID = '-'
AUTH_TOKEN = '-'


def check_rain():
    for forecast in response.json()['list']:
        if [weather for weather in forecast['weather'] if weather['id'] < 700]:
            return True


def send_sms(body):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_='-',
        body=body,
        to='-'
    )


# Fetch weather information
settings = {
    'appid': API_KEY,
    'lat': LAT,
    'lon': LON,
    'units': 'metric',
    'cnt': 4
}

response = requests.get(ENDPOINT, settings)

response.raise_for_status()

# Send SMS alert
if check_rain():
    send_sms("Looks like rain! Bring and umbrella today!")
else:
    send_sms("No rain in sight! Have a nice day!")

