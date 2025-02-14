from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_required, current_user
from app import db
from models.UserLog import UserLog



log_bp = Blueprint("logs", __name__, template_folder="user_logs_templates")

def log_action(user_id, action ,item_id, quantity=None):
    ip_address = request.remote_addr  # Capture user's IP
    new_log = UserLog(user_id=user_id, action=action, item_id=item_id, ip_address=ip_address, quantity=quantity)
    db.session.add(new_log)
    db.session.commit()
    
    

log_bp.route('/', methods=['GET'])
def logs_index():
    all_log = UserLog.query.all()
    
    return render_template('user_log_index.html', all_log=all_log)
