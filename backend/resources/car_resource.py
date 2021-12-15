from db import db
from flask import jsonify
from flask_restful import Resource
from models.car import Car
from schema.car_schema import CarSchema
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
