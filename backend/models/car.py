from . import db


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False)
    production_date = db.Column(db.DateTime, nullable=True)
    licence_number = db.Column(db.String(10), nullable=False)
