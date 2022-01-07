from flask import render_template, redirect, request
from flask_app import app
from models import author

@app.route("/authors")
def Authors():
    authors = author.Author.GetAllAuthors()
    return render_template("authors.html", authors=authors)

@app.route("/authors/add", methods=["POST"])
def AuthorsAdd():
    author.Author.Add(request.form)
    return redirect("/authors")

@app.route("/authors/<int:author_id>")
def AuthorsShow(author_id):
    data = {
        "author_id" : author_id
    }

    author_obj = author.Author.GetAuthor(data)
    non_favorite_books = author.Author.GetNonFavorites(data)
    return render_template("authors_show.html", author_obj=author_obj, non_favorite_books=non_favorite_books)

@app.route("/authors/<int:author_id>/add_favorite", methods=["POST"])
def AuthorsAddFavorite(author_id):
    data = {
        "book_id" : request.form["book_id"],
        "author_id" : author_id
    }
    
    author.Author.AddFavorite(data)
    return redirect(f"/authors/{author_id}")