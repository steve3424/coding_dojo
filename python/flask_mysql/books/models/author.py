from config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, db_row) -> None:
        self.first_name = db_row["first_name"]
        self.last_name = db_row["last_name"]

    @classmethod
    def GetAllAuthors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL("books_db").query_db(query)
        return [cls(row) for row in results]

    @classmethod
    def Add(cls, data):
        query = ("INSERT INTO authors (first_name, last_name, created_at, updated_at)"
                 "VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());")
        connectToMySQL("books_db").query_db(query, data)