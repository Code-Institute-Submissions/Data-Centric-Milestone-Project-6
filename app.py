import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# This sets up our Environment variables in order to run our web app
# and access the database at MongoDB Atlas.
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# This sets up our basic routing through our apps folder structure.
@app.route("/")

# Routes to our Login template
@app.route("/login")

# Allows the user to login with their pre-existing username and password.
def login():
    return render_template("login.html")


# This allows the user to no longer be the active-user, and removes session cookies.
@app.route("/logout")
def logout():
    return redirect(render_template("login.html"))

# Routes to our Register template, and allows the user to create a new username
# and password.
@app.route("/register")
def register():
    return render_template("register.html")

# Routes to the create a character profile template.
@app.route("/create")
def create():
    return render_template("create.html")

# Displays a list of created character profiles from the database.
@app.route("/characters")
def characters():
    return render_template("characters.html")