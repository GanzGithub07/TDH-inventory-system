from flask import Blueprint, render_template, request, url_for, redirect, flash
from models.User import User
from flask_login import login_user, logout_user
from blueprints.Auth.auth_forms import LoginForm

# If `auth_form.py` is in the `blueprints` folder



auth_bp = Blueprint("auth", __name__, template_folder='auth_templates', static_folder='auth_static')

@auth_bp.route('/', methods=['GET'])
def index():
    form = LoginForm()
    
    return render_template('index.html', form=form) 

   

@auth_bp.route('/auth_user',methods=['POST'])
def auth_user():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard.index'))  # Replace 'home' with your desired route
        else:
            flash('Invalid username or password.', 'error')
            return redirect(url_for('auth.index'))
            
@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))