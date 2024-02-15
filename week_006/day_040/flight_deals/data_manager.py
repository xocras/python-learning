import requests

import custom_logging as logging


class DataManager:
    def __init__(self):
        self.SHEETY_AUTH_TOKEN = '-'

        self.SHEETY_HEADERS = {'Authorization': f'Bearer {self.SHEETY_AUTH_TOKEN}'}

        self.PRICES_PATH = '-'

        self.USERS_PATH = '-'

    def get_users(self):
        response = requests.get(self.USERS_PATH, self.SHEETY_HEADERS)

        logging.info(response.text)

        response.raise_for_status()

        return response.json()['users']

    def add_user(self, parameters):
        response = requests.post(
            self.USERS_PATH,
            json=parameters,
            headers=self.SHEETY_HEADERS
        )

        logging.info(response.text)

        response.raise_for_status()

    def get_locations(self):
        response = requests.get(self.PRICES_PATH, self.SHEETY_HEADERS)

        logging.info(response.text)

        response.raise_for_status()

        return response.json()['prices']

    def update_locations(self, row, parameters):
        response = requests.put(
            f'{self.PRICES_PATH}/{row}',
            json=parameters,
            headers=self.SHEETY_HEADERS
        )

        logging.info(response.text)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            logging.error("Update Failed. Try Again.")
