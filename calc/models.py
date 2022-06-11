from calc import db, login_manager
from flask_login import UserMixin

""" DB models settings. """


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)


class Variable(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    value = db.Column(db.Float(), nullable=False)
    desc = db.Column(db.String(length=100), nullable=False, unique=True)

    def __repr__(self):
        return f"Variable {self.name}"
