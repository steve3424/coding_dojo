'''
This is the main file which starts the server. 

It should reference the controllers since it needs to set up all the routing information.

It should reference the app object to run.
'''

from flask_app import app
from flask import render_template, session
from flask_app.controllers import users

@app.route("/")
def index():
    '''
    Redirecting here will clear session UNLESS it gets here
    through a flash validation path. Because flashes only live 
    through 1 redirect, the next redirect will clear the session
    also. This seems like a hacky way to save some form data
    through flash errors, but it works. Users will be logged out
    as soon as they redirect here. There are other, more intelligent
    ways to do this, but it's fine for this assignment.

    TODO: This should probably be dealt w/ client side. Javascript should
    handle the first level of checks that DONT clear the form, while flashes
    SHOULD clear the form w/ error list.
    '''
    if "_flashes" not in session:
        session.clear()
    return render_template("index.html")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
