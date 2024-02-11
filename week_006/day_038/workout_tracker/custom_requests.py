import requests

import custom_logging as logging


def get(endpoint: str, parameters: dict, headers: dict = None) -> dict:

    response = requests.get(endpoint, json=parameters, headers=headers)

    logging.info(response.text)

    response.raise_for_status()

    return response.json()


def post(endpoint: str, parameters: dict, headers: dict = None):

    response = requests.post(endpoint, json=parameters, headers=headers)

    logging.info(response.text)

    response.raise_for_status()

    return response.json()


def put(endpoint: str, parameters: dict, headers: dict = None):
    response = requests.put(endpoint, json=parameters, headers=headers)

    logging.info(response.text)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        logging.error("Update Failed. Try Again.")


def delete(endpoint: str, headers: dict = None):
    response = requests.delete(endpoint, headers=headers)

    logging.info(response.text)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        logging.error("Update Failed. Try Again.")
