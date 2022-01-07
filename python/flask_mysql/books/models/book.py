from config.mysqlconnection import connectToMySQL
from models import author

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_pages = data["num_pages"]
        self.favorited_by = []

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

    @classmethod
    def GetBook(cls, data):
        query = ("SELECT * FROM books "
                 "LEFT JOIN favorites "
                 "ON books.id=favorites.book_id "
                 "LEFT JOIN authors "
                 "ON favorites.author_id=authors.id "
                 "WHERE books.id=%(book_id)s;")
        favorited_by = connectToMySQL("books_db").query_db(query, data)

        # Use first result to create book obj
        book_data = {
            "id" : favorited_by[0]["id"],
            "title" : favorited_by[0]["title"],
            "num_pages" : favorited_by[0]["num_pages"]
        }
        book_obj = cls(book_data)
        
        # Add all authors who favorited
        for row in favorited_by:
            if row["authors.id"] != None:
                author_data = {
                    "id" : row["authors.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"]
                }
                book_obj.favorited_by.append(author.Author(author_data))
        return book_obj

    @classmethod
    def GetNotFavoritedBy(cls, data):
        query = ("SELECT * FROM authors "
                 "WHERE id NOT IN ( "
                    "SELECT author_id FROM favorites "
                    "WHERE book_id=%(book_id)s "
                 ");")
        results = connectToMySQL("books_db").query_db(query, data)
        return [author.Author(row) for row in results]