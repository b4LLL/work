import datetime
from flask import Flask, render_template 
# render template is used for returning htmls upon request

app = Flask(__name__)       #saying webApp is going to be a Flask
                            # application, __name__ simply means this file
@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"
