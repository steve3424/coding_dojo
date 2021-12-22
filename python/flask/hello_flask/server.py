from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:word>")
def Say(word):
    return f"Hi {word.capitalize()}"

@app.route("/repeat/<int:num>/<string:word>")
def Repeat(num, word):
    return f"{word * num}"

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
