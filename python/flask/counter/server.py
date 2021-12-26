from flask import Flask, render_template, redirect, session

app = Flask(__name__)

@app.route("/")
def hello():
    if 'num_visits' in session:
        session['num_visits'] += 1
    else:
        session['num_visits'] = 1

    return render_template("index.html", num_visits=session["num_visits"])

@app.route("/add_2")
def add_2():
    # Add one here, will add the second one on the redirect
    session['num_visits'] += 1
    return redirect("/")

@app.route("/add_num")
def add_num():
    return redirect("/")

@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.secret_key = "super_secret"
    app.run(debug=True)