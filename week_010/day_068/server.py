from os import getenv
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(model_class=Base)

db.init_app(app)


# CONFIGURE TABLE

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template("register.html", message="This e-mail is already in use.")

        user = User(
            name=request.form.get('name'),
            password=request.form.get('password'),
            email=email
        )

        db.session.add(user)

        db.session.commit()

        return render_template("secrets.html", user=user)

    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    return redirect(url_for('home'))


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
