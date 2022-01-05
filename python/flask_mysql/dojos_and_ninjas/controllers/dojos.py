from flask import render_template, request, redirect
from flask_app import app
from models.dojo import Dojo

@app.route("/dojos")
def Dojos():
    # Get all Dojos from db
    dojos = Dojo.GetAll()
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/add", methods=["POST"])
def DojosAdd():
    data = {
        "name" : request.form["dojo_name"]
    }
    Dojo.Add(data) 
    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def DojosShow(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    ninjas = Dojo.GetNinjas(data)
    dojo_name = Dojo.GetName(data)
    return render_template("dojo_ninjas.html", ninjas=ninjas, dojo_name=dojo_name)