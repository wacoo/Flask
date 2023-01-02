""" 
Install flask using pip install flask,
write the following code, 
then run with python interface3.py
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    #i.e if user is not authorised:
    return redirect(url_for("user", name="Wac!"))
if __name__ == '__main__':
    app.run();
