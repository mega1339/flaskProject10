from app import db
from app import app


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   email = db.Column(db.String(), unique=True, nullable=False)
   login = db.Column(db.String(), unique=True, nullable=False)
   password = db.Column(db.String(), unique=False, nullable=False)

@staticmethod
def add(email, login, password):
    with app.app_context():
        db.create_all()
        user = User(email=email, login=login, password=password)
        db.session.add(user)
        db.session.commit()
