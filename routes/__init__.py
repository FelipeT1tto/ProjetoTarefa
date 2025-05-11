from .auth_routes import auth_bp
from .task_routes import task_bp
from .note_routes import note_bp
from .client_routes import client_bp
from .reminder_routes import reminder_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(note_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(reminder_bp)
