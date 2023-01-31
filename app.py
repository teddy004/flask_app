from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def hello_world():
    return "<h1>Well come to the Home Page!</h1>"

@app.route("/about/")
def about():
    return "<h1>Well come to about page</h1>"

@app.route("/capitalize/<word>/")
def capitalize(word):
    return "<h1>{}</h1>".format(escape(word.capitalize()))

@app.route("/add/<int:n1>/<int:n2>")
def add(n1, n2):

    return "<h1>{}</h1>".format(n1 + n2)

