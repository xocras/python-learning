from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "SECRET_KEY"


class LoginForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(8)])
    submit = SubmitField('Log In')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html', login_form=LoginForm())


@app.route('/login', methods=['POST'])
def submit():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return '<h1>It works!</h1>'
    return render_template('login.html', login_form=login_form)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
