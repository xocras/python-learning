import requests

from bs4 import BeautifulSoup


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en'
    }

    url = 'https://www.amazon.com/Nintendo-Switch-OLED-Model-Neon-Joy/dp/B098RL6SBJ'

    response = requests.get(url, headers=headers)

    document = BeautifulSoup(response.text, 'html.parser')

    price = document.select_one('.a-offscreen').getText()

    print(f'Your item price is {price}')


if __name__ == '__main__':
    main()
