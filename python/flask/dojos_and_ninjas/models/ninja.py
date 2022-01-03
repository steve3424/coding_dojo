from config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self):
        pass

    @classmethod
    def Add(cls, data):
        query = ("INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)"
                 "VALUES(%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), NULL)")
        res = connectToMySQL("dojos_and_ninjas_db").query_db(query, data)
        print(res)