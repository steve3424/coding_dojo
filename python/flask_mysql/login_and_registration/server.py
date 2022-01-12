'''
This is the main file which starts the server. 

It should reference the controllers since it needs to set up all the routing information.

It should reference the app object to run.
'''

from flask_app import app
# TODO: Import controllers so the app.route() can be set up
# TODO: Import anything from flask that may be needed 
from flask import render_template, session
from flask_app.controllers import users

@app.route("/")
def index():
    if "_flashes" not in session:
        # TODO: not sure how this will work with user sessions
        session.clear()
    return render_template("index.html")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)