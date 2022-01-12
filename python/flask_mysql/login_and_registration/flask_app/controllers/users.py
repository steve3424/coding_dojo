from flask import redirect, request, session
from flask.templating import render_template
from flask_app import app
from flask_app.models.user import User

@app.route("/register_user", methods=["POST"])
def RegisterUser():
    # store in session so a flash redirect doesn't clear the form
    session["reg_first_name"]       = request.form["first_name"]
    session["reg_last_name"]        = request.form["last_name"]
    session["reg_email"]            = request.form["email"]

    if not User.ValidateRegistrationForm(request.form):
        return redirect("/")
    else:
        data = {
            "first_name" : request.form["first_name"],
            "last_name"  : request.form["last_name"],
            "email"      : request.form["email"],
            "password"   : request.form["password"]
        }
        session["user_id"]    = User.Add(data)
        session["first_name"] = request.form["first_name"]
        session["last_name"]  = request.form["last_name"]
        session["email"]      = request.form["email"]
        return redirect("/login_success")

@app.route("/login_user", methods=["POST"])
def LoginUser():
    # store in session so a flash redirect doesn't clear the form
    session["login_email"] = request.form["email"]

    user_login = User.GetUser(request.form)
    if not user_login:
        return redirect("/")
    else:
        session["user_id"]    = user_login.id
        session["first_name"] = user_login.first_name 
        session["last_name"]  = user_login.last_name 
        session["email"]      = user_login.email 
        return redirect("/login_success")

@app.route("/login_success")
def LoginSuccess():
    if "user_id" in session:
        return render_template("login_success.html", name=session["first_name"])
    else:
        return redirect("/")