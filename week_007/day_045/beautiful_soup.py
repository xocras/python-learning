from bs4 import BeautifulSoup


def main():
    with open('./website.html', encoding='utf-8') as website:
        soup = BeautifulSoup(website.read(), 'html.parser')

        print(soup.title)

        print(soup)

        print(soup.prettify())

        print(soup.findAll(name='a'))
        print([a.getText() for a in soup.findAll(name='a')])
        print([a.get("href") for a in soup.findAll(name='a')])

        print(soup.find(name='h1', id='name').getText())
        print(soup.find(name='h3', class_='heading').getText())

        print(soup.select_one('#name').getText())
        print(soup.select('.heading'))


if __name__ == '__main__':
    main()
