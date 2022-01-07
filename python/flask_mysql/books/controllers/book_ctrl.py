from flask import render_template, redirect, request
from flask_app import app
from models import book

@app.route("/books")
def Books():
    books = book.Book.GetAllBooks()
    return render_template("books.html", books=books)

@app.route("/books/add", methods=["POST"])
def BooksAdd():
    book.Book.Add(request.form)
    return redirect("/books")

@app.route("/books/<int:book_id>")
def BooksShow(book_id):
    data = {
        "book_id" : book_id 
    }
    book_obj = book.Book.GetBook(data)
    not_favorited_by = book.Book.GetNotFavoritedBy(data)
    return render_template("books_show.html", book=book_obj, not_favorited_by=not_favorited_by)