import requests

import custom_logging as logging


class FlightSearch:

    def __init__(self):
        self.KIWI_API_KEY = '-'

        self.KIWI_HEADERS = {'apikey': self.KIWI_API_KEY}

        self.KIWI_LOCATIONS_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'

        self.KIWI_SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'

    def get_code(self, city: str):

        parameters = {
            'term': city,
            'location_types': 'city',
        }

        response = requests.get(
            self.KIWI_LOCATIONS_ENDPOINT,
            headers=self.KIWI_HEADERS,
            params=parameters
        )

        logging.info(response.text)

        return response.json()['locations'][0]['code']

    def find(self, parameters: dict):
        return requests.get(
            self.KIWI_SEARCH_ENDPOINT,
            headers=self.KIWI_HEADERS,
            params=parameters
        ).json()



