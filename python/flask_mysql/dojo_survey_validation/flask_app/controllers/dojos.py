from flask import render_template, session, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def Index():
    if "_flashes" not in session:
        session.clear()
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def Process():
    session["name"]     = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]

    if not Dojo.ValidateDojoForm(request.form):
        return redirect("/")
    else:
        Dojo.Add(request.form)
        return redirect("/result")

@app.route("/result")
def Result():
    dojo = Dojo(session)
    return render_template("result.html", dojo=dojo)