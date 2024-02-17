from selenium import webdriver

from selenium.webdriver.common.by import By


def main():
    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Launch website

    browser = webdriver.Chrome(options=settings)

    browser.get('https://9gag.com/')

    # Find elements

    tabs = browser.find_elements(By.CLASS_NAME, 'home-tab-bar__tab')

    for tab in tabs:
        print(tab.text)


if __name__ == '__main__':
    main()
