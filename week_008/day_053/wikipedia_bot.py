from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def main():
    # Browser parameters

    website = 'https://en.wikipedia.org/wiki/Main_Page'

    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Open website

    browser = webdriver.Chrome(options=settings)

    browser.get(f'{website}')

    # Set timeout

    wait = WebDriverWait(browser, 3600)

    # Run JavaScript

    logo = 'img[alt="Wikipedia"]'

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, logo)))

    with open('./random_article.js') as script:
        browser.execute_script(script.read())

    title = browser.execute_script('return document.querySelector("h1").innerText')

    browser.execute_script(f'alert("Here\'s your article: {title}")')


if __name__ == '__main__':
    main()
