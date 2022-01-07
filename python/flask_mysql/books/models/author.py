from config.mysqlconnection import connectToMySQL
from models import book

class Author:
    def __init__(self, db_row) -> None:
        self.id = db_row["id"]
        self.first_name = db_row["first_name"]
        self.last_name = db_row["last_name"]
        self.favorite_books = []

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
        query = ("SELECT * FROM authors " 
                 "LEFT JOIN favorites ON authors.id=favorites.author_id "
                 "LEFT JOIN books ON favorites.book_id=books.id "
                 "WHERE authors.id=%(author_id)s;")
        favorited_books = connectToMySQL("books_db").query_db(query, data)

        # Use first result to create author
        author_data = {
            "id" : favorited_books[0]["id"],
            "first_name" : favorited_books[0]["first_name"],
            "last_name" : favorited_books[0]["last_name"]
        }
        author = cls(author_data)

        # Add all favorited books
        for row in favorited_books:
            if row["books.id"] != None:
                book_data = {
                    "id" : row["books.id"],
                    "title" : row["title"],
                    "num_pages" : row["num_pages"]
                }
                author.favorite_books.append(book.Book(book_data))
        return author

    @classmethod
    def GetNonFavorites(cls, data):
        query = ("SELECT * FROM books " 
                 "WHERE books.id NOT IN ("
                     "SELECT book_id FROM favorites WHERE author_id=%(author_id)s "
                 ");")
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

    @classmethod
    def AddFavorite(cls, data):
        query = ("INSERT INTO favorites (book_id, author_id) "
                 "VALUES (%(book_id)s, %(author_id)s);")
        connectToMySQL("books_db").query_db(query, data)
