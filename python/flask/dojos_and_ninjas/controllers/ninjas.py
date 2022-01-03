from flask import render_template, request, redirect
from flask_app import app
from models.ninja import Ninja

@app.route("/ninjas")
def Ninjas():
    # Get all dojos from DB
    return render_template("ninjas.html")

@app.route("/ninjas/add", methods=["POST"])
def NinjasAdd():
    # Need to get dojo id
    # Get ninja info from form
    data = {
        "first_name" : request.form["first_name"],
        "last_name"  : request.form["last_name"],
        "age"        : request.form["age"]
    }
    Ninja.Add(data)
    return redirect("/")