import os

import requests

import urllib.request

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup


def download_images(url, folder_path):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("\nFailed to fetch the URL.\n")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all IMG tags
    img_tags = soup.select('a > img')

    # Check images
    if not img_tags:
        print("\nNo images found.\n")
        return

    # Create a folder to save the images if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Iterate through each IMG tag
    for img in img_tags:

        # Get the SRC attribute which contains the image URL
        img_url = img.parent.get('href')

        # Only download JPEG/JPG/PNG/GIF images
        if not (img_url.lower().endswith('.jpeg') or img_url.lower().endswith('.jpg') or
                img_url.lower().endswith('.png') or img_url.lower().endswith('.gif')):
            continue

        # If the image URL is relative, convert it to absolute URL
        if img_url.startswith('/'):
            img_url = urljoin(url, img_url)

        # Extract the filename from the URL
        filename = os.path.join(folder_path, os.path.basename(urlparse(img_url).path))

        # Download the image
        urllib.request.urlretrieve(img_url, filename)
        print(f"• Downloaded: {filename}")


website_url = '-'
download_folder = '-'

download_images(website_url, download_folder)
