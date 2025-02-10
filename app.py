from flask import Flask
from config import DevConfig
from extensions import db, login_manager, migrate
from blueprints.Auth.auth_routes import auth_bp
from blueprints.Dashboard.dashboard_routes import dashboard_bp
from models.User import User
from models.Item import Item




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
    
    #userloader
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    
    return app




if __name__ == '__main__':
    app = create_app()
    app.run()