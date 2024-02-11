# Workout App
# https://developer.nutritionix.com/admin/access_details
import logging

import custom_requests as requests

from datetime import datetime

from os import environ


def nutritionix_request(query):

    app_id = environ.get('NUTRITIONIX_APP_ID')

    api_key = environ.get('NUTRITIONIX_API_KEY')

    host_domain = "https://trackapi.nutritionix.com"

    endpoint = f"{host_domain}/v2/natural/exercise"

    headers = {
        'x-app-id': app_id,
        'x-app-key': api_key
    }

    parameters = {
        'query': query
    }

    return requests.post(endpoint, parameters, headers)


def add_rows(data):
    auth_token = environ.get('SHEETY_AUTH_TOKEN')

    worksheet_path = environ.get('WORKSHEET_PATH')

    host_domain = "https://api.sheety.co"

    endpoint = f"{host_domain}/{worksheet_path}"

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    today = datetime.now()

    date = today.strftime('%m/%d/%Y')

    time = today.strftime('%H:%M:%S')

    for exercise in data['exercises']:
        parameters = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': exercise['user_input'].title(),
                'duration': exercise['duration_min'],
                'calories': exercise['nf_calories']
            }
        }

        requests.post(endpoint, parameters, headers)


def main():
    response = nutritionix_request("swam for 2 hours and lifted weights for 45 minutes")

    add_rows(response)


if __name__ == '__main__':
    main()
