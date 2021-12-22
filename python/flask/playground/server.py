from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/play")
def Play():
    return render_template("blue.html")

@app.route("/play/<int:num>/<string:col>")
def PlayNum(num, col):
    return render_template("blue.html", num=num, col=col)

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
