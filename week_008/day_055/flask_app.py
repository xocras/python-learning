from flask import Flask

from random import randint

app = Flask(__name__)

answer = randint(1, 10)


def make_heading(f):
    def return_heading():
        return f'<h1>{f()}</h1>'
    return return_heading


def add_image(f):
    def add_image_tag():
        return f'{f()}<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    return add_image_tag


@app.route('/')
@add_image
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
