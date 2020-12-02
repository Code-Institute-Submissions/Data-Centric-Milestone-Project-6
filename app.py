# Sets up our imported libraries and resources to be used in the app.
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# Assigns a flask app, to the variable app.
app = Flask(__name__)

# This sets up our Environment variables in order to run our web app
# and access the database at MongoDB Atlas.
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Tells the app to assign Pymongo to the variable: mongo, of which the global
# app variable is already assigned within parenthesis, to Pymongo.
mongo = PyMongo(app)


# This is a Guard code.
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
        # check if user exists in the database.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Checks if the chosen username already exists ("Truthy") in the database, and if
        # so, flashes an error message.
        if existing_user:
            flash("Username unavailable!")
            return redirect(url_for("register"))

        # Providing the active-user's inputs pass the above check,
        # Insert their chosen credentials into the database with MongoDB,
        # To then be stored and recalled at a later date, when the user wishes
        # To Log back in.
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Puts the new user into a "session" cookie as cached data.
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
                # In event of an incorrect password input, flash a message and
                # redirect the user to the login.html template page.
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # If the Username input by user doesn't exist, flash message
            # and redirect to the login.html template.
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# This allows the user to no longer be the active-user, and removes
# session cookies.
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Routes to the create a character profile template.
@app.route("/create", methods=["GET", "POST"])
def create():
    # Datasets assigned from MongoDB to local variables, in order to then be
    # used on the create.html template.
    positive = (mongo.db.positive.find())
    negative = (mongo.db.negative.find())
    talents = (mongo.db.talents.find())
    genders = mongo.db.genders.find()
    rank = mongo.db.rank.find()
    builds = mongo.db.builds.find()
    backstory = mongo.db.backstory.find()

    # If a POST method id called (user clicks the create button), then
    # app takes the data from inout fields in the create.html by the same
    # key names as the dict below, stores this data in the variable 'character'
    if request.method == "POST":
        character = {
            "name": request.form.get("name"),
            "title": request.form.get("title"),
            "rank": request.form.get("rank"),
            "image": request.form.get("image"),
            "species": request.form.get("species"),
            "gender": request.form.get("gender"),
            "age": request.form.get("age"),
            "hair": request.form.get("hair"),
            "build": request.form.get("build"),
            "talents": request.form.get("talents"),
            "traits": request.form.get("traits"),
            "backstory": request.form.get("backstory"),
            "authored_by": session["user"]
        }
        # Then this line inserts these key value pairs using the variable.
        # 'character' which has the data stored, and inserts it in the
        # appropriate collection on MongoDB.
        mongo.db.characters.insert_one(character)
        # Then once the above is complete, a flash image appears telling the
        # user that they have successfully created their character on site.
        flash("Character Created!")
        # And then the page redirects to the main characters page, where the
        # user can see their own creation newly inserted onto the page.
        return redirect(url_for("characters"))

    # This renders the create.html template using the variables called from
    # MongoDB that we created above.
    return render_template(
        "create.html", positive=positive,
         negative=negative, talents=talents, genders=genders,
         rank=rank, builds=builds, backstory=backstory)


# Displays a list of created character profiles from the database.
@app.route("/characters")
def characters():
    # Finds and assigns all datasets within the characters collection
    # on MongoDB to a local variable, so they can be displayed, in the
    # characters.html template.
    characters = mongo.db.characters.find()
    return render_template("characters.html", characters=characters)

@app.route("/edit_character<character_id>", methods=["GET", "POST"])
def edit_character(character_id):

    positive = (mongo.db.positive.find())
    negative = (mongo.db.negative.find())
    talents = (mongo.db.talents.find())
    genders = mongo.db.genders.find()
    rank = mongo.db.rank.find()
    builds = mongo.db.builds.find()
    backstory = mongo.db.backstory.find()

    if request.method == "POST":
        submit = {
            "name": request.form.get("name"),
            "title": request.form.get("title"),
            "rank": request.form.get("rank"),
            "image": request.form.get("image"),
            "species": request.form.get("species"),
            "gender": request.form.get("gender"),
            "age": request.form.get("age"),
            "hair": request.form.get("hair"),
            "build": request.form.get("build"),
            "talents": request.form.get("talents"),
            "traits": request.form.get("traits"),
            "backstory": request.form.get("backstory"),
            "authored_by": session["user"]
        }
        mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
        flash("Character Updated!")
        return redirect(url_for("characters"))

    character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
    return render_template("edit_character.html", character=character,
         positive=positive, negative=negative, talents=talents, genders=genders,
         rank=rank, builds=builds, backstory=backstory)