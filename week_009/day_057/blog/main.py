import requests

from datetime import datetime

from flask import Flask, render_template


app = Flask(__name__)

YEAR = datetime.now().year
AUTHOR = 'Oscar Cruz'
RESPONSE = requests.get('https://api.npoint.io/8bd72c17fef7761df73b').json()


@app.route('/')
def index():

    return render_template(
        "index.html",
        author=AUTHOR,
        year=YEAR,
        response=RESPONSE
    )


@app.route('/post/<int:post_id>')
def post(post_id):

    blog_post = next((blog_post for blog_post in RESPONSE if blog_post['id'] == post_id), None)

    return render_template(
        "post.html",
        author=AUTHOR,
        year=YEAR,
        blog_post=blog_post
    )


if __name__ == "__main__":
    app.run(debug=True)
