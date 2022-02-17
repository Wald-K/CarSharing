from models import db
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from resources.car_resource import CarsItemResource, CarsListResource

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:!QAZ2wsx@localhost:5432/car_sharing"

db.init_app(app)
api = Api(app)
migrate = Migrate(app, db)


api.add_resource(CarsListResource, '/api/cars')
api.add_resource(CarsItemResource, "/api/cars/<car_id>")

if __name__ == "__main__":
    app.run(debug=True)
