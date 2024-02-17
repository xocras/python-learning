import time

import urllib.request

from urllib.parse import urlparse

from selenium import webdriver

from selenium.webdriver import Keys

from selenium.webdriver.common.by import By


def main():
    #  Set website

    domain = '-'

    sub_domain = '-'

    page = '-'

    # Set folder path

    folder_path = "-"

    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Open website

    browser = webdriver.Chrome(options=settings)

    browser.get(f'{domain}{sub_domain}{page}')

    # Scroll down

    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    time.sleep(10)

    # Fetch thumbnails

    images = browser.find_elements(By.CSS_SELECTOR, '.home_container .small_pin_box img')

    # Set headers

    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': f'{domain}{sub_domain}{page}'}

    # Download images

    for i, image in enumerate(images):

        # Extract source

        src = image.get_attribute('src')

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


if __name__ == '__main__':
    main()
