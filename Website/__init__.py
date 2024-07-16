from flask import Flask
from .extensions import db
from .models import User, Recipe
from flask_login import LoginManager
from flask_migrate import Migrate
from .auth import auth as auth_blueprint
from .recipes import recipes as recipes_blueprint
import os

def create_app():
    app = Flask(__name__)

    base_dir = os.path.dirname(__file__)
    secret_key_path = os.path.join(base_dir, "secret_key")
    with open(secret_key_path, "r") as f:
        app.config['SECRET_KEY'] = f.readline().strip()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'users': 'sqlite:///path/to/users.db',
        'recipes': 'sqlite:///path/to/recipes.db'
    }

    # Configuration setup
    db.init_app(app)

    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(recipes_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        # Return the user object or None
        return User.query.get(int(user_id))

    return app
