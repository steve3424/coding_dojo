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
    return render_template("books_show.html")