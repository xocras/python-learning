import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def main():
    # Browser parameters

    website = 'https://tinder.com/app/recs'

    #  Keep browser instance open

    settings = webdriver.ChromeOptions()

    settings.add_experimental_option('detach', True)

    # Open website

    browser = webdriver.Chrome(options=settings)

    browser.get(f'{website}')

    # Set timeout

    wait = WebDriverWait(browser, 3600)

    # Send clicks every couple of seconds

    like = '[style="transform: scale(1); background-color: rgba(16, 224, 132, 0);"]'

    dislike = '[style="transform: scale(1); background-color: rgba(253, 84, 108, 0);"]'

    try:
        while True:

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, like)))

            browser.find_element(By.CSS_SELECTOR, dislike).click()

            time.sleep(2)

    except KeyboardInterrupt:
        # Press (Ctrl+C) to exit the loop gracefully
        pass

    finally:
        # Close the browser
        browser.quit()


if __name__ == '__main__':
    main()
