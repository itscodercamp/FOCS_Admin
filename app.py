import os
from flask import Flask
from flask_cors import CORS
from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(app.instance_path, 'database.db')}")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'projects'), exist_ok=True)

    # Enable CORS for all routes - Allow all origins
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
            "expose_headers": ["Content-Type", "Authorization"],
            "supports_credentials": False,
            "max_age": 3600
        }
    })

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'

    # Register Blueprints
    from routes.main import main_bp
    from routes.api import api_bp
    from routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Create tables
    with app.app_context():
        db.create_all()
        create_initial_admin()

    return app

def create_initial_admin():
    from models import User
    from werkzeug.security import generate_password_hash
    
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        hashed_password = generate_password_hash('admin123', method='scrypt')
        new_admin = User(username='admin', password_hash=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print("Initial admin created: admin/admin123")

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app = create_app()
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
