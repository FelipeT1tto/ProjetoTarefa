from flask import Blueprint, render_template, request, redirect, session, url_for
from models import get_user, create_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tasks.dashboard'))
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user(request.form['username'], request.form['password'])
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('tasks.dashboard'))
        return render_template('login.html', error='Credenciais inválidas')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        create_user(request.form['username'], request.form['password'])
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
