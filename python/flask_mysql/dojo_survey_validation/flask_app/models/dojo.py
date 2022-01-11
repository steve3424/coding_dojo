from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data) -> None:
        self.name     = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comments = data["comments"]

    @classmethod
    def Add(cls, dojo_form):
        query = ("INSERT INTO dojos (name,location,language,comment,created_at,updated_at) "
                 "VALUES (%(name)s, %(location)s, %(language)s, %(comments)s, NOW(), NOW())")
        connectToMySQL("dojo_survey_schema").query_db(query, dojo_form)

    @staticmethod
    def ValidateDojoForm(form):
        is_valid = True
        if len(form["name"]) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(form["location"]) == 0:
            flash("Must choose a location")
            is_valid = False
        if len(form["language"]) == 0:
            flash("Must choose language")
            is_valid = False
        if len(form["comments"]) == 0:
            flash("Must add comments")
            is_valid = False
        return is_valid