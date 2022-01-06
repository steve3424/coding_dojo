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
    # TODO: Can pass in name instead of a separate db call here
    author_obj = author.Author.GetName(author_id)

    data = {
        "author_id" : author_id
    }
    favorite_books = author.Author.GetFavorites(data)
    return render_template("authors_show.html", author_obj=author_obj, favorite_books=favorite_books)