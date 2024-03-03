import requests
from os import environ
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"

Bootstrap5(app)


db = SQLAlchemy(model_class=Base)

db.init_app(app)


tmdb_api_key = environ.get('TMDB_API_KEY')

tmdb_url = 'https://api.themoviedb.org/3'


class Movie(db.Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 10', name='check_rating'),
        CheckConstraint('ranking > 0 AND rating <= 10', name='check_ranking')
    )

    def __repr__(self):
        return f'<Movie  {self.title}, {self.year}, {self.description}>'


class MovieAddForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired(), Length(0, 250)])
    submit = SubmitField('Add Movie')


class MovieEditForm(FlaskForm):
    rating = DecimalField('Rating:', validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField('Review:', validators=[DataRequired(), Length(0, 250)])
    submit = SubmitField('Update Movie')


@app.route('/')
def index():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    for i, movie in enumerate(movies[::-1]):
        movie.ranking = i + 1

    return render_template('index.html', movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieAddForm()

    if form.validate_on_submit():

        params = {
            'api_key': tmdb_api_key,
            'query': form.title.data
        }

        endpoint = f'{tmdb_url}/search/movie'

        response = requests.get(endpoint, params=params)

        if response.status_code != 200:
            return render_template('add.html', form=form)

        data = response.json()

        if not data['results']:
            return render_template('add.html', form=form)

        movies = data['results']

        return select(movies)

    return render_template('add.html', form=form)


@app.route('/new/<int:movie_id>/edit', methods=['GET', 'POST'])
def new(movie_id):
    form = MovieEditForm()

    params = {
        'api_key': tmdb_api_key
    }

    endpoint = f'{tmdb_url}/movie/{movie_id}'

    movie = requests.get(endpoint, params=params).json()

    if form.validate_on_submit():

        movie = Movie(
            title=movie['title'],
            year=movie['release_date'].split('-')[0],
            description=movie['overview'][:250].strip() + '...',
            rating=movie['vote_average'],
            ranking=10,
            review='',
            img_url=f'https://image.tmdb.org/t/p/w500{movie['poster_path']}',
        )

        db.session.add(movie)

        db.session.commit()

        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()

        return redirect(url_for('index'))

    return render_template("edit.html", movie=movie, form=form)


@app.route('/select-movie')
def select(movies):
    return render_template('select.html', movies=movies)


@app.route('/movie/<int:movie_id>/edit', methods=['GET', 'POST'])
def edit(movie_id):
    form = MovieEditForm()

    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()

        return redirect(url_for('index'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/book/<int:movie_id>/delete", methods=["GET", "POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)

    db.session.delete(movie)

    db.session.commit()

    return redirect(url_for('index'))


def main():

    with app.app_context():
        db.create_all()

    app.run(debug=True)


if __name__ == "__main__":
    main()
