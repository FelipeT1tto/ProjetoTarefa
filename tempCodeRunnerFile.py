from flask import Flask
from models import init_db
from routes.auth import auth_bp
from routes.tasks import tasks_bp
from routes.notes import notes_bp
import os

app = Flask(__name__)
app.secret_key = 'secreta'

# Inicializa banco se não existir
if not os.path.exists('database.db'):
    init_db()

# Registra blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)
app.register_blueprint(notes_bp)

if __name__ == '__main__':
    app.run(debug=True)
