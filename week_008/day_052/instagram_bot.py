from selenium import webdriver


def main():
    # Browser parameters

    website = 'https://www.instagram.com/'

    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Open website

    browser = webdriver.Chrome(options=settings)

    browser.get(f'{website}')


if __name__ == '__main__':
    main()
