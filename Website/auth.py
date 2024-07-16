from flask_login import login_user, current_user, login_required, logout_user
from flask import Blueprint, request, flash, redirect, url_for, render_template
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from . import db
import re

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Logged in successfully!", category="success")
            return redirect(url_for('views.home'))
        else:
            flash("Incorrect email or password, try again.", category="error")

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", category="success")
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash("Invalid email address.", category="error")
            return render_template("sign_up.html", user=current_user)

        if User.query.filter_by(email=email).first():
            flash("Email already exists.", category="error")
        elif len(firstName) < 2 or len(lastName) < 2:
            flash("Name must be more than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            try:
                new_user = User(email=email, firstName=firstName, lastName=lastName,
                                password=generate_password_hash(password1, method="pbkdf2:sha256"))
                db.session.add(new_user)
                db.session.commit()
                flash("Account created! Please log in.", category="success")
                return redirect(url_for("auth.login"))
            except Exception as e:
                flash("An error occurred. Please try again.", category="error")
                print(e)  # For debugging purposes, consider logging this instead

    return render_template("sign_up.html", user=current_user)
