""" 
Install flask using pip install flask,
write the following code, 
then run with python interface2.py
"""

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/admin")
def admin():
    #i.e if user is not authorised:
    return redirect(url_for("home"))
if __name__ == '__main__':
    app.run();
