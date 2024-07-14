from flask import Flask
from .extensions import db
from .auth import auth as auth_blueprint, generate_password_hash

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = generate_password_hash('secret', method="pbkdf2:sha256")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_BINDS'] = {
        'recipes': 'sqlite:///recipes.db'
    }
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    app.register_blueprint(auth_blueprint)

    return app

def run_app(app):
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

