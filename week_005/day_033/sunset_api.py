import requests

settings = {
    'lat': 0,
    'lng': 0,
    'date': "today",
    'tzid': '-'
}

response = requests.get("https://api.sunrise-sunset.org/json", settings)

response.raise_for_status()

sunrise, sunset = response.json()['results']['sunrise'], response.json()['results']['sunset']

print(f"\nSunrise: {sunrise}\nSunset: {sunset}")
