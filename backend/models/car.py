from sqlalchemy.exc import IntegrityError

from . import db


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String, nullable=False)
    production_date = db.Column(db.DateTime, nullable=True)
    licence_number = db.Column(db.String(10), nullable=False)

    @classmethod
    def create_car(cls, new_car):
        created = False
        car_db = Car(
            model=new_car["model"],
            production_date=new_car["production_date"],
            licence_number=new_car["licence_number"],
        )
        db.session.begin_nested()
        try:
            db.session.add(car_db)
            db.session.commit()
            created = True
            return created
        except IntegrityError:
            db.session.rollback()
            db.session.refresh(car_db)
            created = False
            return created
