from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Recipe
from .extensions import db

recipes = Blueprint('recipes', __name__)

@recipes.route('/add-recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        recipe = Recipe(name=name,
                        description=description,
                        ingredients=ingredients,
                        instructions=instructions,
                        user_id=current_user.id
                        )
        db.session.add(recipe)
        db.session.commit()
        flash('Recipe added successfully!', category='success')
        return redirect(url_for('views.home'))
    return render_template('add_recipe.html', user=current_user)


