from flask import Blueprint, render_template, request, redirect, session, url_for
from models import get_all_notes, add_note, delete_note, update_note

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    if request.method == 'POST':
        add_note(user_id, request.form['title'], request.form['content'])
        return redirect(url_for('notes.notes'))
    all_notes = get_all_notes(user_id)
    return render_template('notes.html', notes=all_notes)

@notes_bp.route('/delete_note/<int:note_id>')
def delete_note_route(note_id):
    delete_note(note_id)
    return redirect(url_for('notes.notes'))

@notes_bp.route('/update_note/<int:note_id>', methods=['POST'])
def update_note_route(note_id):
    update_note(note_id, request.form['title'], request.form['content'])
    return redirect(url_for('notes.notes'))
