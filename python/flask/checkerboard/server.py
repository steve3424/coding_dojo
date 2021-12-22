from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Checkerboard():
    return render_template("index.html", rows=8, cols=8, color_1="red", color_2="blue")

@app.route("/<int:rows>")
def Checkerboard_1(rows):
    return render_template("index.html", rows=rows, cols=8, color_1="red", color_2="blue")

@app.route("/<int:rows>/<int:cols>")
def Checkerboard_2(rows, cols):
    return render_template("index.html", rows=rows, cols=cols, color_1="red", color_2="blue")

@app.route("/<int:rows>/<int:cols>/<string:color_1>")
def Checkerboard_3(rows, cols, color_1):
    return render_template("index.html", rows=rows, cols=cols, color_1=color_1, color_2="blue")

@app.route("/<int:rows>/<int:cols>/<string:color_1>/<string:color_2>")
def Checkerboard_4(rows, cols, color_1, color_2):
    return render_template("index.html", rows=rows, cols=cols, color_1=color_1, color_2=color_2)

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
