from flask import Flask
from config import DevConfig
from extensions import db, login_manager, migrate
from blueprints.Auth.auth_routes import auth_bp
from blueprints.Dashboard.dashboard_routes import dashboard_bp
from blueprints.Item.item_routes import item_bp
from blueprints.UserLog.user_log_routes import log_bp
from models.User import User
from models.Item import Item
from models.UserLog import UserLog




def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig) 

    #extentions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    
    #blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(item_bp, url_prefix='/item')
    app.register_blueprint(log_bp, url_prefix='/test_logs')
    
    #userloader
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run()