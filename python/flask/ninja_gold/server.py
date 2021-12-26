from flask import Flask, render_template, redirect, request, session
import random
from datetime import datetime

app = Flask(__name__)

def GetGold(min,max,lose_gold=False):
    factor = 1
    if lose_gold:
        if random.randint(0, 1) == 0:
            factor = -1

    gold = random.randint(min,max) * factor
    return gold

def Log(prev_gold, current_gold, building):
    date_string = str(datetime.now())
    format = "%m/%d/%Y %I:%M %p"
    current_dt = datetime.now().strftime(format)
    net_gold = current_gold - prev_gold
    if net_gold < 0:
        return (f"Entered a casino and lost {net_gold * -1} " 
                f"golds... Ouch... ({current_dt})"), "red"
    elif net_gold == 0:
        return (f"Entered a casino and won"
                f"nothing... ({current_dt})"), "black"
    else:
        return (f"Earned {net_gold} golds from "
                f"the {building}! ({current_dt})"), "green"

@app.route("/")
def Main():
    if "gold" not in session:
        session["gold"] = 0
    if "log" not in session:
        session["log"] = []
    return render_template("index.html", gold=session["gold"], log=session["log"])

@app.route("/process_money", methods=["POST"])
def ProcessMoney():
    prev_gold = session["gold"]
    if   request.form["building"] == "farm":
        session["gold"] += GetGold(10,20)
    elif request.form["building"] == "cave":
        session["gold"] += GetGold(5,10)
    elif request.form["building"] == "house":
        session["gold"] += GetGold(2,5)
    elif request.form["building"] == "casino":
        session["gold"] += GetGold(0,50,lose_gold=True)

    log_string,color = Log(prev_gold, session["gold"], request.form["building"])
    session["log"].append({"color":color, "string":log_string})

    return redirect("/")

@app.route("/clear_session")
def ClearSession():
    session.clear()
    return redirect("/")

@app.errorhandler(404)
def ERR(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.secret_key = "key"
    app.run(debug=True)