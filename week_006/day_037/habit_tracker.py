import custom_logging as logging

import custom_requests as requests

PIXELA_USER = "-"
PIXELA_TOKEN = "-"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"


def create_user():
    parameters = {
        'token': PIXELA_TOKEN,
        'username': PIXELA_USER,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    requests.post(PIXELA_ENDPOINT, parameters)


def create_graph(parameters):
    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    # parameters = {
    #     'id': 'id',
    #     'name': 'name',
    #     'unit': 'units',
    #     'type': 'type',
    #     'color': 'color',
    #     'timezone': 'timezone'
    # }

    requests.post(GRAPH_ENDPOINT, parameters, headers)

    logging.info(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{parameters['id']}.html")


def add_pixel(parameters: dict, graph_id: str):
    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    # parameters = {
    #     'date': 'date'
    #     'quantity': 'quantity',
    # }

    requests.post(f"{GRAPH_ENDPOINT}/{graph_id}", parameters, headers)

    logging.info(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}.html")


def update_pixel(parameters, graph_id, date):
    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    # parameters = {
    #     'quantity': 'quantity',
    # }

    requests.put(f"{GRAPH_ENDPOINT}/{graph_id}/{date}", parameters, headers)

    logging.info(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}.html")


def delete_pixel(graph_id, date):
    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    requests.delete(f"{GRAPH_ENDPOINT}/{graph_id}/{date}", headers)

    logging.info(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}.html")
