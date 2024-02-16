import pandas

import requests

from bs4 import BeautifulSoup

website = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

html = requests.get(website).text

document = BeautifulSoup(html, 'html.parser')

movies = [title.getText() for title in document.select('h3.title')]

pandas.DataFrame(movies[::-1]).to_csv('best_movies.csv', header=False, index=False)
