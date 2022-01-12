import re
from flask import flash
import flask_app
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self) -> None:
        pass

    @classmethod
    def ValidateRegistrationForm(cls, registration_form):
        is_valid = True

        first_name = registration_form["first_name"]
        if len(first_name) < 2:
            flash("First name should be at least 2 characters")
            is_valid = False
        elif not first_name.isalpha():
            flash("First name should contain only alphabetical characters")
            is_valid = False

        last_name = registration_form["last_name"]
        if len(last_name) < 2:
            flash("Last name should be at least 2 characters")
            is_valid = False
        elif not last_name.isalpha():
            flash("Last name should contain only alphabetical characters")
            is_valid = False

        email = registration_form["email"]
        if not cls.email_regex.match(email):
            flash("Invalid email address")
            is_valid = False
        elif cls.EmailExists(registration_form):
            flash("Email already registered")
            is_valid = False

        password = registration_form["password"]
        confirm_password = registration_form["confirm_password"]
        if len(password) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        elif len(password) > 64:
            flash("Password should be less than 64 characters")
            is_valid = False
        elif password != confirm_password:
            flash("Passwords do not match")
            is_valid = False
        
        return is_valid

    @classmethod
    def EmailExists(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_and_reg_db").query_db(query,data)
        return len(results) > 0