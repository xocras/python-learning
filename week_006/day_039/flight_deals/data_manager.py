import requests

import custom_logging as logging


class DataManager:
    def __init__(self):
        self.SHEETY_AUTH_TOKEN = '-'

        self.SHEETY_HEADERS = {'Authorization': f'Bearer {self.SHEETY_AUTH_TOKEN}'}

        self.WORKSHEET_PATH = '-'

    def get_locations(self):
        response = requests.get(self.WORKSHEET_PATH, self.SHEETY_HEADERS)

        logging.info(response.text)

        response.raise_for_status()

        return response.json()['prices']

    def update_locations(self, row, parameters):
        response = requests.put(
            f'{self.WORKSHEET_PATH}/{row}',
            json=parameters,
            headers=self.SHEETY_HEADERS
        )

        logging.info(response.text)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            logging.error("Update Failed. Try Again.")
