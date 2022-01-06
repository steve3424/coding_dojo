from config.mysqlconnection import connectToMySQL
from models import book

class Author:
    def __init__(self, db_row) -> None:
        self.id = db_row["id"]
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

    @classmethod
    def GetAuthor(cls, data):
        query = "SELECT * FROM authors WHERE id=%(author_id)s;"
        result = connectToMySQL("books_db").query_db(query, data)
        return cls(result[0])

    @classmethod
    def GetFavorites(cls, data):
        query = ("SELECT * FROM authors " 
                 "JOIN favorites ON authors.id=favorites.author_id "
                 "JOIN books ON favorites.book_id=books.id "
                 "WHERE authors.id=%(author_id)s;")
        favorite_books = connectToMySQL("books_db").query_db(query, data)
        fav_book_objs = []
        for row in favorite_books:
            book_data = {
                "id" : row["books.id"],
                "title" : row["title"],
                "num_pages" : row["num_pages"]
            }
            fav_book_objs.append(book.Book(book_data))
        return fav_book_objs

    @classmethod
    def GetNonFavorites(cls, data):
        query = ("SELECT * FROM books " 
                 "LEFT JOIN favorites ON books.id=favorites.book_id "
                 "WHERE favorites.author_id != %(author_id)s;")
        non_fav_books = connectToMySQL("books_db").query_db(query, data)
        non_fav_book_objs = []
        for row in non_fav_books:
            book_data = {
                "id" : row["id"],
                "title" : row["title"],
                "num_pages" : row["num_pages"]
            }
            non_fav_book_objs.append(book.Book(book_data))
        return non_fav_book_objs