""" 
Install flask using pip install flask,
write the following code, 
then run with python interface4.py
"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template("index.html", content=name, r=2, lst=["wac", "lil","dag", "bish", "bark"])

if __name__ == '__main__':
    app.run();
