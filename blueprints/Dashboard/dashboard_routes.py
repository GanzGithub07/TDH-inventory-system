from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required
# If `auth_form.py` is in the `blueprints` folder



dashboard_bp = Blueprint("dashboard", __name__, template_folder='dashboard_templates', static_folder='dashboard_static')

@dashboard_bp.route('/')
@login_required
def index():
    return render_template('dashboard_index.html')




