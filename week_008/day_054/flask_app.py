from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    with open('./motivational_poster.html') as html:
        return html.read()


def main():
    app.run()


if __name__ == '__main__':
    main()
