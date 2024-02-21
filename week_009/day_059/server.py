import requests

from flask import Flask, render_template

RESPONSE = requests.get('https://api.npoint.io/8bd72c17fef7761df73b').json()
AUTHOR = 'Oscar Cruz'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        response=RESPONSE,
        author=AUTHOR
    )


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def blog_post(post_id):

    post = next((post for post in RESPONSE if post['id'] == post_id), None)

    return render_template(
        'post.html',
        author=AUTHOR,
        post=post
    )


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
