from flask import render_template, request, redirect
from flask_app import app
from models.ninja import Ninja
from models.dojo import Dojo

@app.route("/ninjas")
def Ninjas():
    dojos = Dojo.GetAll()
    return render_template("ninjas.html", dojos=dojos)

@app.route("/ninjas/add", methods=["POST"])
def NinjasAdd():
    data = {
        "dojo_id"    : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name"  : request.form["last_name"],
        "age"        : request.form["age"]
    }
    Ninja.Add(data)
    return redirect("/")