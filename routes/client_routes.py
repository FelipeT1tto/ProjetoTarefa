from flask import Blueprint, render_template, request, redirect
import client_manager

client_bp = Blueprint('client_bp', __name__)

@client_bp.route("/clients", methods=["GET", "POST"])
def clients():
    if request.method == "POST":
        client_manager.add_client(
            request.form["name"],
            request.form["email"]
        )
        return redirect("/clients")
    return render_template("clients.html", clients=client_manager.list_clients())
