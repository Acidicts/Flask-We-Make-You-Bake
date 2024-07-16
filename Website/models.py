from . import db
from flask_login import UserMixin
from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    firstName = db.Column(db.String(30), nullable=True)  # Ensure this matches how it's used
    lastName = db.Column(db.String(30), nullable=True)
    is_authenticated = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

    def get_id(self):
        """
        Return the email address to satisfy Flask-Login's requirements.
        """
        return self.id

# Recipe model for recipes.db
class Recipe(db.Model):
    __bind_key__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

