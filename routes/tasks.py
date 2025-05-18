from flask import Blueprint, render_template, request, redirect, session, url_for
from models import get_tasks, add_task, delete_task, update_task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

@tasks_bp.route('/tasks')
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    tarefas = get_tasks(user_id)
    return render_template('tasks.html', tasks=tarefas)

@tasks_bp.route('/add_task', methods=['POST'])
def add_task_route():
    user_id = session['user_id']
    add_task(user_id, request.form['title'], request.form['description'], request.form['date'], request.form['importance'])
    return redirect(url_for('tasks.tasks'))

@tasks_bp.route('/delete_task/<int:task_id>')
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect(url_for('tasks.tasks'))

@tasks_bp.route('/update_task/<int:task_id>', methods=['POST'])
def update_task_route(task_id):
    update_task(task_id, request.form['title'], request.form['description'], request.form['date'], request.form['importance'])
    return redirect(url_for('tasks.tasks'))
