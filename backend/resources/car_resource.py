from flask import jsonify, request
from flask_restful import Resource
from models import db
from models.car import Car
from schema.car_schema import CarCreateRequest, CarSchema
from werkzeug.exceptions import NotFound


class CarsItemResource(Resource):
    def get(self, car_id):
        car = db.session.query(Car).filter(Car.id == car_id).first()
        if car is None:
            raise NotFound(f"car with id={car_id} not found")

        schema = CarSchema()
        return schema.dump(car)


class CarsListResource(Resource):
    def get(self):
        cars = db.session.query(Car).order_by(Car.id).all()
        schema = CarSchema(many=True)
        return schema.dump(cars)

    def post(self):
        schema = CarCreateRequest()
        data = request.get_json()
        new_car = schema.load(data)

        is_created = Car.create_car(new_car)

        if is_created:
            db.session.commit()
            return CarSchema().dump(new_car)
        else:
            return jsonify({"message": "Car not created"})
