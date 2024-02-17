from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def main():
    # Browser parameters

    website = 'https://www.instagram.com/'

    user = '-'

    password = '-'

    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Open website

    browser = webdriver.Chrome(options=settings)

    browser.get(f'{website}')

    # Set timeout

    wait = WebDriverWait(browser, 3600)


if __name__ == '__main__':
    main()
