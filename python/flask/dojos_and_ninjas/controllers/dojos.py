from flask import render_template, request, redirect
from flask_app import app

@app.route("/dojos")
def Dojos():
    # Get all Dojos from db
    return render_template("dojos.html")