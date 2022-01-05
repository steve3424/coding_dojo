from config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, db_row):
        self.first_name = db_row["first_name"]
        self.last_name = db_row["last_name"]
        self.age = db_row["age"]

    @classmethod
    def Add(cls, data):
        query = ("INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)"
                 "VALUES(%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);")
        res = connectToMySQL("dojos_and_ninjas_db").query_db(query, data)
        print(res)