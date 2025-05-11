from flask import Blueprint, render_template, request, redirect, session

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect('/')
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/register')
