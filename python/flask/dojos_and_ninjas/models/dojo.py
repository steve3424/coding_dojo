from config.mysqlconnection import connectToMySQL

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