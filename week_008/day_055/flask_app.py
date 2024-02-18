from flask import Flask

from random import randint

app = Flask(__name__)

answer = randint(1, 10)


@app.route('/')
def home():
    return 'Choose a number!'


@app.route(f'/{answer}')
def correct():
    return f'You found me!'


@app.route('/<int:number>')
def choice(number):
    return 'Too high!' if number > answer else 'Too low!'


@app.route('/user/<name>/<int:age>')
def user(name, age):
    return f'Your name is {name} and you are {age} years old.'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
