import requests

from bs4 import BeautifulSoup

website = 'https://news.ycombinator.com/'

html = requests.get(website).text

document = BeautifulSoup(html, 'html.parser')

titles = [
    {
        'title': row.select_one('.titleline > a').getText(),
        'url': row.select_one('.titleline > a').get('href'),
        'score': row.findNext('tr').select_one('.score').getText().split()[0]
        if row.findNext('tr').select_one('.score') else 0
    }
    for row in document.select('.athing')
]

titles.sort(key=lambda i: int(i['score']), reverse=True)

print(titles[0])
