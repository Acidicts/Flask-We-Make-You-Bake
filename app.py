from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

DB_NAME = "users.db"
DB_NAME2 = "recipes.db"

users = SQLAlchemy()
recipes = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = "unknown jkl"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_DATABASE_URI_2'] = f'sqlite:///{DB_NAME2}'

users.init_app(app)
recipes.init_app(app)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
