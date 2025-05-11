from flask import Blueprint, render_template, request, redirect
import notes

note_bp = Blueprint('note_bp', __name__)

@note_bp.route("/notes", methods=["GET", "POST"])
def notes_page():
    if request.method == "POST":
        notes.add_note(request.form["content"])
        return redirect("/notes")
    return render_template("notes.html", notes=notes.list_notes())

@note_bp.route("/delete_note/<int:note_id>")
def delete_note_route(note_id):
    notes.delete_note(note_id)
    return redirect("/notes")
