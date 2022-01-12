import re
from flask import flash
from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self, data) -> None:
        self.id         = data["id"]
        self.first_name = data["first_name"]
        self.last_name  = data["last_name"]
        self.email      = data["email"]

    @classmethod
    def ValidateRegistrationForm(cls, registration_form):
        is_valid = True

        first_name = registration_form["first_name"]
        if len(first_name) < 2:
            flash("First name should be at least 2 characters", "register_flashes")
            is_valid = False
        elif not first_name.isalpha():
            flash("First name should contain only alphabetical characters", "register_flashes")
            is_valid = False

        last_name = registration_form["last_name"]
        if len(last_name) < 2:
            flash("Last name should be at least 2 characters", "register_flashes")
            is_valid = False
        elif not last_name.isalpha():
            flash("Last name should contain only alphabetical characters", "register_flashes")
            is_valid = False

        email = registration_form["email"]
        if not cls.email_regex.match(email):
            flash("Invalid email address", "register_flashes")
            is_valid = False
        elif cls.EmailExists(registration_form):
            flash("Email already registered", "register_flashes")
            is_valid = False

        password = registration_form["password"]
        confirm_password = registration_form["confirm_password"]
        if len(password) < 8:
            flash("Password must be at least 8 characters", "register_flashes")
            is_valid = False
        elif len(password) > 64:
            flash("Password should be less than 64 characters", "register_flashes")
            is_valid = False
        elif password != confirm_password:
            flash("Passwords do not match", "register_flashes")
            is_valid = False
        
        return is_valid

    @classmethod
    def GetUser(cls,login_form):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_and_reg_db").query_db(query,login_form)

        if len(results) == 0:
            flash(f"User {login_form['email']} not found!", "login_flashes")
            return None
        elif not bcrypt.check_password_hash(results[0]["password"], login_form["password"]):
            flash("Password is incorrect!", "login_flashes")
            return None
        else:
            return cls(results[0])

    @classmethod
    def EmailExists(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_and_reg_db").query_db(query,data)
        return len(results) > 0

    @classmethod
    def Add(cls, data):
        data["password"] = bcrypt.generate_password_hash(data["password"])
        query = ("INSERT INTO users (first_name,last_name,email,password,created_at,updated_at)"
                 "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());")
        return connectToMySQL("login_and_reg_db").query_db(query,data)