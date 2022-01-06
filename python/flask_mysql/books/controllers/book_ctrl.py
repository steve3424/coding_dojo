import re
from flask import render_template, redirect, request
from flask_app import app

@app.route("/books")
def Books():
    return render_template("books.html")