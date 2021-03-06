from flask import Flask, render_template, redirect, session, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def Users():
    users = User.GetAll()
    return render_template("users.html", users=users)

@app.route("/users/new")
def UsersNew():
    return render_template("users_new.html")

@app.route("/user_add", methods=["POST"])
def UserAdd():
    data = {
        "first_name" : request.form["fname"],
        "last_name"  : request.form["lname"],
        "email"      : request.form["email"]
    }

    User.Add(data)

    return redirect("/users")

@app.route("/user_update", methods=["POST"])
def UserUpdate():
    data = {
        "id"         : request.form["id"],
        "first_name" : request.form["fname"],
        "last_name"  : request.form["lname"],
        "email"      : request.form["email"]
    }
    User.Update(data)
    return redirect(f"/users/{request.form['id']}")

@app.route("/users_delete/<int:user_id>")
def UserDelete(user_id):
    User.Delete(user_id)
    return redirect("/users")

@app.route("/users/<int:user_id>")
def UserShow(user_id):
    user = User.GetUserFromID(user_id)
    return render_template("show.html", user=user)

@app.route("/users/<int:user_id>/edit")
def UserEdit(user_id):
    user = User.GetUserFromID(user_id)
    return render_template("user_edit.html", user=user)

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
