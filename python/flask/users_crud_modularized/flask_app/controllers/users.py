from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/users")
def UsersAll():
    users = User.GetAll()
    return render_template("users.html", users=users)

@app.route("/users/<int:user_id>")
def UsersShow(user_id):
    user = User.GetUserFromID(user_id)
    return render_template("users_show.html", user=user)

@app.route("/users_delete/<int:user_id>")
def UserDelete(user_id):
    User.Delete(user_id)
    return redirect("/users")

@app.route("/users_update", methods=["POST"])
def UserUpdate():
    data = {
        "id"         : request.form["id"],
        "first_name" : request.form["fname"],
        "last_name"  : request.form["lname"],
        "email"      : request.form["email"]
    }
    User.Update(data)
    return redirect(f"/users/{request.form['id']}")

@app.route("/users/new")
def UsersNew():
    return render_template("users_new.html")

@app.route("/users_add", methods=["POST"])
def UserAdd():
    data = {
        "first_name" : request.form["fname"],
        "last_name"  : request.form["lname"],
        "email"      : request.form["email"]
    }
    User.Add(data)
    return redirect("/users")