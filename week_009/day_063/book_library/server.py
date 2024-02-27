from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap5(app)

books = []


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), Length(0, 250)])
    author = StringField('Book Author', validators=[DataRequired(), Length(0, 250)])
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(0, 10)])
    submit = SubmitField('Add Book')


@app.route('/')
def index():
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():

        book = {
            'name': form.name.data,
            'author': form.author.data,
            'rating': form.rating.data
        }

        books.append(book)

        print(books)

        return index()

    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

