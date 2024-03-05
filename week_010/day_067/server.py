from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from os import getenv


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(model_class=Base)

db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/<int:post_id>')
def show_post(post_id):
    post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=post)


@app.route('/add', methods=['GET', 'POST'])
def add_post():

    if request.method == 'GET':
        return render_template("make-post.html")

    post = BlogPost(
        title='',
        subtitle='',
        date='',
        body='',
        author='',
        img_url='',
    )

    db.session.add(post)

    db.session.commit()

    return show_post(post.id)


@app.route('/<int:post_id>', methods=['PATCH'])
def edit_post(post_id):
    post = db.session.get(BlogPost, post_id)

    post.title = ''

    return render_template("post.html", post=post)


@app.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)

    db.session.delete(post)

    db.session.commit()

    return get_all_posts()


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
