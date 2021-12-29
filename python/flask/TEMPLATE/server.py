from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
