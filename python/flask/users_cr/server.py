from flask import Flask, render_template, redirect, session, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def Users():
    users = User.GetAll()
    return render_template("index.html", users=users)

@app.route("/users/new")
def UsersNew():
    return render_template("users_new.html")

@app.route("/user_add", methods=["POST"])
def UserAdd():
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.Add(data)

    return redirect("/users")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
