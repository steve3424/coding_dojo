'''
This is the main file which starts the server. It should reference the 
controllers since it needs to set up all routing information.
'''

from flask import redirect
from flask_app import app
from controllers import author_ctrl
from controllers import book_ctrl

@app.route("/")
def index():
    return redirect("/authors")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
