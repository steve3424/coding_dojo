
from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id         = data["id"]
        self.first_name = data["first_name"]
        self.last_name  = data["last_name"]
        self.email      = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def GetAll(cls):
        full_table = connectToMySQL("users_db").query_db("SELECT * FROM users")
        for u in full_table:
            print(u)
        users = [cls(row) for row in full_table]
        return users
    
    @classmethod
    def GetUserFromID(cls, user_id):
        query = "SELECT * FROM users WHERE id=%(user_id)s"
        data = {
            "user_id" : user_id
        }
        user = connectToMySQL("users_db").query_db(query, data)
        return cls(user[0])

    @classmethod
    def Add(cls, data):
        query = ("INSERT INTO users (first_name, last_name, email, created_at, updated_at)" 
                "VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW())")
        return connectToMySQL("users_db").query_db(query, data)