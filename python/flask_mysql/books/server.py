'''
This is the main file which starts the server. It should reference the 
controllers since it needs to see all the routing information.
'''

from flask import render_template, redirect, session, request
from flask_app import app
from controllers import author_ctrl

@app.route("/")
def index():
    return redirect("/authors")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
