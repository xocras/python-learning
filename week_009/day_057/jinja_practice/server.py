import requests

from random import randint

from datetime import datetime

from flask import Flask, render_template

AUTHOR = 'Oscar Cruz'

YEAR = datetime.now().year

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        author=AUTHOR,
        year=YEAR,
        random=randint(1, 10)
    )


@app.route('/guess')
def guess():
    return render_template(
        'guess.html',
        author=AUTHOR,
        year=YEAR
    )


@app.route('/guess/<name>')
def guess_result(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']

    return render_template(
        'guess.html',
        author=AUTHOR,
        year=YEAR,
        name=name.title(),
        age=age,
        gender=gender
    )


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/8bd72c17fef7761df73b').json()

    return render_template(
        'blog.html',
        author=AUTHOR,
        year=YEAR,
        response=response
    )


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
