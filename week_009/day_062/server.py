from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])

    location = URLField('Location URL', validators=[DataRequired(), URL()])

    open_time = TimeField('Open Time', validators=[DataRequired()])

    close_time = TimeField('Closing Time', validators=[DataRequired()])

    coffee_rating = SelectField(
        'Coffee Rating',
        validators=[DataRequired()],
        choices=[('☕' * n if n else '❌', '☕' * n if n else '❌') for n in range(6)]
    )
    wifi_rating = SelectField(
        'Wi-Fi Rating',
        validators=[DataRequired()],
        choices=[('💪🏻' * n if n else '❌', '💪🏻' * n if n else '❌') for n in range(6)])

    outlet_rating = SelectField(
        'Power Outlet Rating',
        validators=[DataRequired()],
        choices=[('🔌' * n if n else '❌', '🔌' * n if n else '❌') for n in range(6)]
    )

    submit = SubmitField('Submit')


# All Flask routes below
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as data:
            row = [
                form.cafe.data,
                form.location.data,
                form.open_time.data,
                form.close_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.outlet_rating.data
            ]
            csv.writer(data).writerow(row)

        return cafes()

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        rows = [row for row in csv_data]
    return render_template('cafes.html', data=rows)


if __name__ == '__main__':
    app.run(debug=True)
