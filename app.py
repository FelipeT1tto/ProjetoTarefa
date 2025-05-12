# app.py
from flask import Flask, session, redirect, url_for
from models import init_db
from auth import auth_bp
from tasks import tasks_bp
from notes import notes_bp
import os

app = Flask(__name__)
app.secret_key = 'secreta'

if not os.path.exists('database.db'):
    init_db()

# Registra os Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)
app.register_blueprint(notes_bp)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks.dashboard'))
    return redirect(url_for('auth.login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
