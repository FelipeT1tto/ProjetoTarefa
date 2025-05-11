from flask import Blueprint, render_template, request, redirect
import reminder

reminder_bp = Blueprint('reminder_bp', __name__)

@reminder_bp.route("/reminders", methods=["GET", "POST"])
def reminders():
    if request.method == "POST":
        reminder.add_reminder(
            request.form["message"],
            request.form["remind_at"]
        )
        return redirect("/reminders")
    return render_template("reminders.html", reminders=reminder.list_reminders())
