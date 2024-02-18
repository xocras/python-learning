from flask import Flask

from random import randint

app = Flask(__name__)

answer = randint(1, 10)


def make_heading(text):
    def return_heading():
        return f'<h1>{text()}</h1>'
    return return_heading


@app.route('/')
@make_heading
def home():
    return 'Choose a number!'


@app.route(f'/{answer}')
def correct():
    with open('./correct.html') as file:
        return file.read()


@app.route('/<int:number>')
def choice(number):
    with open(f'./{'too_high' if number > answer else 'too_low'}.html') as file:
        return file.read()


@app.route('/user/<name>/<int:age>')
def user(name, age):
    return f'Your name is {name} and you are {age} years old.'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
