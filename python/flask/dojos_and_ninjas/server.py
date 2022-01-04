'''
This is the main file which starts the server. It should reference the 
controllers since it needs to see all the routing information.
'''

from flask import redirect
from flask_app import app
from controllers import ninjas
from controllers import dojos

@app.route("/")
def index():
    return redirect("/dojos")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
