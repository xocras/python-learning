from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "SECRET_KEY"

EMAIL = 'admin@email.com'
PASSWORD = '12345678'


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
        if login_form.email.data == EMAIL and login_form.password.data == PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', login_form=login_form)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
