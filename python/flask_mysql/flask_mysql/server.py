from flask import Flask, render_template
from author import Author

app = Flask(__name__)

@app.route("/")
def hello():
    authors = Author.get_all()
    return render_template("index.html", authors=authors)

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
