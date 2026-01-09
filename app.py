from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from users import USERS
from decorators import login_required

app = Flask(__name__)
app.secret_key = "CHANGE_THIS_TO_A_RANDOM_SECRET"

@app.route("/", methods=["GET"])
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in USERS and check_password_hash(USERS[email], password):
            session["logged_in"] = True
            session["user"] = email
            return redirect("/dashboard")
        else:
            error = "Invalid login credentials"

    return render_template("login.html", error=error)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
