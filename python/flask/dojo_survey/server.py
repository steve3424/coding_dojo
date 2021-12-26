from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/")
def Main():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def Process():
    session["name"]     = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/result")

@app.route("/result")
def Result():
    return render_template("result.html", name=session["name"], location=session["location"], language=session["language"], comments=session["comments"])

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.secret_key = "cantguessthis"
    app.run(debug=True)
