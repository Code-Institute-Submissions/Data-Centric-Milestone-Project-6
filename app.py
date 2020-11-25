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

# Routes to our Register template, and allows the user to create a new username
# and password.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("characters", username=session["user"]))

    return render_template("register.html")


# Routes to our Login template.
# Allows the user to login with their pre-existing username and password.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks if username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checks if the hashed password (in the Monogo Database),
            # matches user input.
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}!".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "characters", username=session["user"]))
            else:
                # In event of an incorrect password input.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If the Username input by user doesn't exist, flash message and redirect.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# This allows the user to no longer be the active-user, and removes session cookies.
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Routes to the create a character profile template.
@app.route("/create")
def create():
    positive = mongo.db.positive.find()
    negative = mongo.db.negative.find()
    talents = mongo.db.talents.find()
    genders = mongo.db.genders.find()
    rank = mongo.db.rank.find()
    builds = mongo.db.builds.find()
    return render_template(
        "create.html", positive=positive,
         negative=negative, talents=talents, genders=genders,
         rank=rank, builds=builds)

# Displays a list of created character profiles from the database.
@app.route("/characters")
def characters():
    characters = mongo.db.characters.find()
    return render_template("characters.html", characters=characters)

