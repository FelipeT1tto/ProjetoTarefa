# notes/__init__.py
from flask import Blueprint, render_template, request, session, redirect, url_for
from models import get_notes, update_note

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    if request.method == 'POST':
        content = request.form['content']
        update_note(user_id, content)
    note = get_notes(user_id)
    return render_template('notes.html', note=note)
