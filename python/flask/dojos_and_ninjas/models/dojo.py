from config.mysqlconnection import connectToMySQL
from models.ninja import Ninja

class Dojo:
    def __init__(self, row) -> None:
        self.id = row["id"]
        self.name = row["name"]

    @classmethod
    def GetAll(cls):
        query = "SELECT id,name FROM dojos;"
        result = connectToMySQL("dojos_and_ninjas_db").query_db(query)
        dojos = [cls(row) for row in result]
        return dojos

    @classmethod
    def Add(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VAlUES (%(name)s, NOW(), NOW())"
        connectToMySQL("dojos_and_ninjas_db").query_db(query, data)

    @classmethod
    def GetNinjas(cls, data):
        query = "SELECT first_name, last_name, age FROM ninjas WHERE dojo_id=%(dojo_id)s;"
        result = connectToMySQL("dojos_and_ninjas_db").query_db(query, data)
        ninjas = [Ninja(row) for row in result]
        return ninjas

    @classmethod
    def GetName(cls, data):
        query = "SELECT name FROM dojos WHERE id=%(dojo_id)s;"
        result = connectToMySQL("dojos_and_ninjas_db").query_db(query, data)
        print(result)
        return result[0]["name"]