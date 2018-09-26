from flask import Flask, render_template, request, session
from flask_session import Session  

#global variables
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "super secret key"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:                #if the note dictionary is not initialised,
        session["notes"] = []                       #then initialise a dictionary that is unique to your session
    if request.method == "POST":                    #if i tried to add a note.. POST method            
        note = request.form.get("note")             #grab the note from the form that was sent to this function
        session["notes"].append(note)               #add a new thing to the list of notes

    return render_template("notes.html", notes=session["notes"])
    


@app.route("/hello", methods=["GET", "POST"])
def hello():
        if request.method == "GET":
                return "Please submit the form instead."
        else:
            name = request.form.get("name")
            return render_template("hello.html", name=name)

