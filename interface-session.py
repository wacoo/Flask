""" 
Install flask using pip install flask,
write the following code, 
then run with python interface4.py
"""

from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Hello"
app.permanent_session_lifetime = timedelta(days=5)
@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        usrx = request.form["nm"]
        session["user"] = usrx
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        #return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run();
