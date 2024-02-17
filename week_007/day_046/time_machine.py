import requests

from bs4 import BeautifulSoup


def main():
    year = input('\nWhich year would you like to travel to? Enter a date (YYYY-MM-DD):\n')

    response = requests.get('https://www.billboard.com/charts/hot-100/' + year)

    response.raise_for_status()

    document = BeautifulSoup(response.text, 'html.parser')

    title_query = '.chart-results-list .o-chart-results-list__item > h3'

    titles = [
        {
            'title': title.getText().strip(),
            'author': title.find_next_sibling().getText().strip()
        } for title in document.select(title_query)
    ]

    for i, title in enumerate(titles):
        print(f'• {i + 1:02} - {title['title']} by {title['author']}')


if __name__ == '__main__':
    main()
