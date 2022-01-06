from config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_pages = data["num_pages"]

    @classmethod
    def GetAllBooks(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL("books_db").query_db(query)
        return [cls(row) for row in results]

    @classmethod
    def Add(cls, data):
        query = ("INSERT INTO books (title, num_pages, created_at, updated_at) "
                 "VALUES (%(title)s, %(num_pages)s, NOW(), NOW());")
        connectToMySQL("books_db").query_db(query, data)