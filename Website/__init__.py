from flask import Flask
from flask_login import LoginManager
from .extensions import db
from .auth import auth as auth_blueprint
from .views import views
from .models import User
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)

    # Constructing the path to 'secret_key.txt' dynamically
    base_dir = os.path.dirname(__file__)
    secret_key_path = os.path.join(base_dir, "secret_key")
    with open(secret_key_path, "r") as f:
        app.config['SECRET_KEY'] = f.readline().strip()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'recipes': 'sqlite:///recipes.db'
    }
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(views)

    @login_manager.user_loader
    def load_user(user_id):
        # Return the user object or None
        return User.query.get(int(user_id))

    return app
