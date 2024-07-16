from flask import render_template, Blueprint, flash
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        flash("You are logged in!", category="success")
    return render_template('index.html', current_user=current_user)
