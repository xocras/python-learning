from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Float, CheckConstraint
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

Bootstrap5(app)

db = SQLAlchemy(app)


class Book(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    author = Column(String(250), nullable=False)
    rating = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 10', name='check_rating'),
    )

    def __repr__(self):
        return f'<Book {self.name}, {self.author}, {self.rating}/10>'


class BookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), Length(0, 250)])
    author = StringField('Book Author', validators=[DataRequired(), Length(0, 250)])
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(0, 10)])
    submit = SubmitField('Add Book')


@app.route('/')
def index():
    books = [
        {
            'name': book.name,
            'author': book.author,
            'rating': f'{book.rating:.1f}' if book.rating % 1 else f'{book.rating:.0f}'
        } for book in Book.query.all()
    ]

    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():

        db.session.add(
            Book(
                name=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
        )

        db.session.commit()

        return index()

    return render_template('add.html', form=form)


def main():
    with app.app_context():
        db.create_all()

    app.run(debug=True)


if __name__ == "__main__":
    main()


