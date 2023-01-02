""" 
Install flask using pip install flask,
write the following code, 
then run with python interface1.py
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True);
