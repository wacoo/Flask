""" 
Install flask using pip install flask,
write the following code, 
then run with python interface4.py
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        usrx = request.form["nm"]
        return redirect(url_for("user", usr=usrx))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run();
