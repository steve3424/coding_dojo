from flask import redirect, request, session
from flask_app import app
from flask_app.models.user import User

@app.route("/register_user", methods=["POST"])
def RegisterUser():
    # store in session so a flash redirect doesn't clear the form
    session["reg_first_name"]       = request.form["first_name"]
    session["reg_last_name"]        = request.form["last_name"]
    session["reg_email"]            = request.form["email"]
    session["reg_password"]         = request.form["password"]
    session["reg_confirm_password"] = request.form["confirm_password"]

    if not User.ValidateRegistrationForm(request.form):
        print("redirect w/ flashes")
    return redirect("/")