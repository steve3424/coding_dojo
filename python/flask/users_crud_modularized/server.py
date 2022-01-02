from flask import redirect
from flask_app import app
from flask_app.controllers import users

@app.route("/")
def index():
    return redirect("/users")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)