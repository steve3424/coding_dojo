'''
This is the main file which starts the server. 

It should reference the controllers since it needs to set up all the routing information.

It should reference the app object to run.
'''

from flask_app import app
# TODO: Import controllers so the app.route() can be set up
# TODO: Import anything from flask that may be needed 

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
