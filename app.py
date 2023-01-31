from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def hello_world():
    return "<h1>Well come to the Home Page!</h1>"

@app.route("/about/")
def about():
    return "<h1>Well come to about page</h1>"