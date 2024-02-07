import requests

PIXELA_USER = "-"
PIXELA_TOKEN = "-"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"


def post_request(endpoint: str, parameters: dict, headers: dict = None):

    response = requests.post(endpoint, json=parameters, headers=headers)

    print(response.text)

    response.raise_for_status()


def create_user():
    parameters = {
        'token': PIXELA_TOKEN,
        'username': PIXELA_USER,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    post_request(PIXELA_ENDPOINT, parameters)


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

    post_request(GRAPH_ENDPOINT, parameters, headers)

    print(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{parameters['id']}.html")


def add_pixel(parameters, graph_id):
    headers = {
        'X-USER-TOKEN': PIXELA_TOKEN
    }

    # parameters = {
    #     'date': 'date'
    #     'quantity': 'quantity',
    # }

    post_request(f"{GRAPH_ENDPOINT}/{graph_id}", parameters, headers)

    print(f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}.html")
