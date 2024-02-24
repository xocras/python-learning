from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "SECRET_KEY"


class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html', login_form=LoginForm())


@app.route('/login', methods=['POST'])
def submit():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>It works!</h1>'
    return render_template('login.html', form=form)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
