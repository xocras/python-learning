from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from os import getenv


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

Bootstrap5(app)

ckeditor = CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = SQLAlchemy(model_class=Base)

db.init_app(app)


# CONFIGURE FORM

class PostForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(0, 250)])
    subtitle = StringField('Subtitle:', validators=[DataRequired(), Length(0, 250)])
    author = StringField('Author:', validators=[DataRequired(), Length(0, 100)])
    img_url = URLField('Blog Image URL:', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content:', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


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


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/<int:post_id>')
def show_post(post_id):
    post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=post)


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()

    if form.validate_on_submit():

        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.today().date().strftime('%B %d, %Y'),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data,
        )

        db.session.add(post)

        db.session.commit()

        return redirect(url_for('show_post', post_id=post.id))

    return render_template("make-post.html", form=form)


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):

    post = db.session.get(BlogPost, post_id)

    form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )

    if form.validate_on_submit():

        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data

        db.session.add(post)

        db.session.commit()

        return redirect(url_for('show_post', post_id=post.id))

    return render_template("make-post.html", form=form, post=post, title="Edit Post")


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = db.session.get(BlogPost, post_id)

    db.session.delete(post)

    db.session.commit()

    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
