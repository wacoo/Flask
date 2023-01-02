""" 
Install flask using pip install flask,
write the following code, 
then run with python interface_inherit.py
"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index2.html')

@app.route("/test")
def test():
    return render_template('new.html')


if __name__ == '__main__':
    app.run(debug=True);
