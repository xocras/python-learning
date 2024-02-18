from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    with open('./motivational_poster.html') as html:
        return html.read()


@app.route("/secret")
def secret():
    return 'Oh, no! You found me.'


def main():
    app.run()


if __name__ == '__main__':
    main()
