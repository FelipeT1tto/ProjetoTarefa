from flask import Blueprint, render_template, request, redirect
import task_manager

task_bp = Blueprint('task_bp', __name__)

@task_bp.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task_manager.add_task(
            request.form["title"],
            request.form["description"],
            request.form["due_date"]
        )
        return redirect("/tasks")
    tasks = task_manager.list_tasks()
    return render_template("tasks.html", tasks=tasks)

@task_bp.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    task_manager.complete_task(task_id)
    return redirect("/tasks")

@task_bp.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect("/tasks")
