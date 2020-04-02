from flask import Flask, request, render_template, session
import random

app = Flask(__name__)

app.secret_key = "12345"

@app.route("/", methods=["GET"])
def pokaż_formularz():
    return render_template("form.html")

@app.route("/", methods=["POST"]) # odbior danych
def przywitaj():
    name = request.form["name"]
    return render_template("hello.html", name=name)

@app.route("/game", methods=["GET"])
def show_form():

    session["secret_key"] = random.randint(1, 10)
    print("My chosen number:", session["secret_key"])
    return render_template("guess.html")

@app.route("/game", methods=["POST"])
def calc():

    answer_ok = False

    try:
        answer = int(request.form["teasing"])
    except ValueError:
        return "! number  (ノಠ益ಠ)ノ彡┻━┻"

    secret_key = session["secret_key"]

    if answer == secret_key:
        answer_ok = True
        emoji = "correct (☆^ー^☆) ! yay (ㆆᴗㆆ) ! "
    elif answer < secret_key:
        emoji = "too low "
    else:
        emoji = "too high"

    return render_template("guess.html", answer=str(answer), answer_ok=answer_ok, emoji=emoji)


app.run()