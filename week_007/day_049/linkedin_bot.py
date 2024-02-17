from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


def main():
    # Browser parameters

    website = 'https://www.linkedin.com/'

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

    # Log in

    user_input = 'input[autocomplete="username"]'

    password_input = 'input[autocomplete="current-password"]'

    signin_button = 'button[data-id="sign-in-form__submit-btn"]'

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, user_input)))

    browser.find_element(By.CSS_SELECTOR, user_input).send_keys(user)

    browser.find_element(By.CSS_SELECTOR, password_input).send_keys(password)

    browser.find_element(By.CSS_SELECTOR, signin_button).click()


if __name__ == '__main__':
    main()
