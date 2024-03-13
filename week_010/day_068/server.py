from os import getenv
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_login import login_user, LoginManager, login_required, current_user, logout_user


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

app.config['UPLOAD_FOLDER'] = './static/files'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(model_class=Base)

db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)


# CONFIGURE USER

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    authenticated: Mapped[bool] = mapped_column(Boolean)
    active: Mapped[bool] = mapped_column(Boolean)
    anonymous: Mapped[bool] = mapped_column(Boolean)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return self.anonymous

    def get_id(self):
        return str(self.id)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


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

        password = request.form.get('password')

        password = generate_password_hash(password, salt_length=8)

        user = User(
            name=request.form.get('name'),
            password=password,
            email=email,
            authenticated=True,
            active=True,
            anonymous=False,
        )

        db.session.add(user)

        db.session.commit()

        login_user(user)

        return render_template("secrets.html", user=user)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')

        user = User.query.filter_by(email=email).first()
        if not user:
            return render_template("login.html", message="This account doesn't exist.")

        password = request.form.get('password')

        if not check_password_hash(user.password, password):
            return render_template("login.html", message="Invalid password.")

        login_user(user)

        return render_template("secrets.html", user=user)

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
