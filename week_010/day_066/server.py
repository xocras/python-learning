from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route('/')
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route('/all', methods=['GET'])
def fetch_all():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/search', methods=['GET'])
def search():
    location = request.args.get('location')

    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()

    if not cafes:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location."})

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/random', methods=['GET'])
def fetch_random():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()

    return jsonify(cafe=choice(cafes).to_dict())


# HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add_cafe():
    return jsonify(response={'Success': 'Successfully added the new cafe.'})


# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')

    cafe = db.session.get(Cafe, cafe_id)

    if not cafe:
        return jsonify(error={'Not Found': "We couldn't find a cafe with the entered ID."}), 404

    cafe.coffee_price = new_price

    return jsonify(response={'Success': 'Successfully updated the price.'}), 200


# HTTP DELETE - Delete Record

@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    api_key = request.args.get('api_key')

    if api_key != 'SECRET_KEY':
        return jsonify(error={'Not Authorized': "Not enough permissions to perform that action."}), 403

    cafe = db.session.get(Cafe, cafe_id)

    if not cafe:
        return jsonify(error={'Not Found': "We couldn't find a cafe with the entered ID."}), 404

    db.session.delete(cafe)

    db.session.commit()

    return jsonify(response={'Success': 'Successfully deleted the cafe from the database.'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
