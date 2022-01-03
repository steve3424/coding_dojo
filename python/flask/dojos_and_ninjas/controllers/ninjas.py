from flask import render_template
from werkzeug.utils import redirect
from flask_app import app

@app.route("/ninjas")
def Ninjas():
    # Get all dojos from DB
    return render_template("ninjas.html")

@app.route("/ninjas/add")
def NinjasAdd():
    # Need to get dojo id
    # Get ninja info from form
    # Call ninja object to add entry to db
    redirect("/")