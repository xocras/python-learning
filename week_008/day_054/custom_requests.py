import requests

import custom_logging as logging


def request_handler(method):
    def handle_request():
        response = method()

        logging.info(response.text)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            logging.error("Request Failed. Try Again.")

        return response.json()

    return handle_request


@request_handler
def get(endpoint: str, parameters: dict, headers: dict = None):
    return requests.get(endpoint, json=parameters, headers=headers)


@request_handler
def post(endpoint: str, parameters: dict, headers: dict = None):
    return requests.post(endpoint, json=parameters, headers=headers)


@request_handler
def put(endpoint: str, parameters: dict, headers: dict = None):
    return requests.put(endpoint, json=parameters, headers=headers)


@request_handler
def delete(endpoint: str, headers: dict = None):
    return requests.delete(endpoint, headers=headers)

