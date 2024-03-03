from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Float, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

Bootstrap5(app)

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

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


class BookEditForm(FlaskForm):
    rating = DecimalField('Rating', validators=[DataRequired(), NumberRange(0, 10)])
    submit = SubmitField('Edit Book')


@app.route('/')
def index():
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()

    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()

    if form.validate_on_submit():

        book = Book(
                name=form.name.data,
                author=form.author.data,
                rating=form.rating.data
        )

        db.session.add(book)

        db.session.commit()

        return redirect(url_for("edit", book_id=book.id))

    return render_template('add.html', form=form)


@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def edit(book_id):
    form = BookEditForm()

    book = db.get_or_404(Book, book_id)

    if form.validate_on_submit():
        book.rating = form.rating.data

        db.session.commit()

        return redirect(url_for('index'))

    return render_template("edit.html", book=book, form=form)


@app.route("/book/<int:book_id>/delete", methods=["GET", "POST"])
def delete(book_id):

    book = db.get_or_404(Book, book_id)

    db.session.delete(book)

    db.session.commit()

    return redirect(url_for('index'))


def main():

    with app.app_context():
        db.create_all()

    app.run(debug=True)


if __name__ == "__main__":
    main()


