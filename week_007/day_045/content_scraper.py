import os

import requests

import urllib.request

import urllib.error

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def download_images(domain, sub, folder_path):

    # Simulate browser
    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': domain + sub}

    # Send a GET request to the URL
    response = requests.get(domain + sub, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print("\nFailed to fetch the URL.\n")
        return

    # Parse the HTML content
    document = BeautifulSoup(response.content, 'html.parser')

    # Find all IMG thumbnails
    img_urls = document.select('.masonry_box.small_pin_box > a')

    # Check images
    if not img_urls:
        print("\nNo images found.\n")
        return

    # Create a folder to save the images if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Iterate through each IMG tag
    for img_url in img_urls:

        # Fetch source of the original image
        response = requests.get(domain + img_url.get('href'))

        # Parse the HTML content
        document = BeautifulSoup(response.content, 'html.parser')

        # Get the SRC attribute which contains the original image URL
        img_url = document.select_one(f'.big_pin_box img[alt="{img_url.get('title')}"]').get('src')

        # If the image URL is relative, convert it to absolute URL
        if img_url.startswith('/'):
            img_url = urljoin(domain, img_url)

        # Extract the filename from the URL
        filename = os.path.join(folder_path, os.path.basename(urlparse(img_url).path))

        try:
            # Create a request object with the URL and headers
            request = urllib.request.Request(img_url, headers=headers)

            # Download the image
            with urllib.request.urlopen(request) as response:
                # Download the image
                with open(filename, 'wb') as file:
                    file.write(response.read())

            print(f"• Downloaded: {filename}")

        except urllib.error.HTTPError:

            print(f"• Error: {img_url}")


website_url = '-'
sub_domain = '-'
download_folder = '-'

download_images(website_url, sub_domain, download_folder)
