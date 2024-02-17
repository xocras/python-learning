import requests

import urllib.request

from bs4 import BeautifulSoup

from urllib.parse import urlparse


def scrape_site(page):
    #  Set website
    domain = '-'

    sub_domain = '/-'

    page = f'/-/?page={page}'

    # Set folder path

    folder_path = "-"

    # Set header

    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': f'{domain}{sub_domain}{page}'}

    # Send a GET request to the URL

    response = requests.get(f'{domain}{sub_domain}{page}', headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print("\nFailed to fetch the URL.\n")
        return

    # Parse the HTML content

    document = BeautifulSoup(response.content, 'html.parser')

    # Fetch thumbnails

    images = document.select('.home_container .small_pin_box > a')

    # Download images

    for i, image in enumerate(images):

        # Extract thumbnail link

        href = image.get('href')

        # Fetch original image

        response = requests.get(f'{domain}{href}', headers=headers)

        # Check if the request was successful
        if response.status_code != 200:
            print("\nFailed to fetch the URL.\n")

        # Parse the HTML content

        document = BeautifulSoup(response.content, 'html.parser')

        image = document.select_one(f'.big_pin_box img')

        # Extract image source

        src = image.get('src')

        # Set file path

        file_path = f'{folder_path}/{urlparse(src).path.split('/')[-1]}'

        # Create a request object with the URL and headers

        request = urllib.request.Request(src, headers=headers)

        # Download the image

        with urllib.request.urlopen(request) as response:
            with open(file_path, 'wb') as download:
                download.write(response.read())

        # Log result
        print(f'• {i + 1}/{len(images)} Downloaded: {file_path}')


def main():
    for n in range(1, 10):
        scrape_site(n)


if __name__ == '__main__':
    main()
