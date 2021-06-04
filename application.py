import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from pow_helpers import apology, login_required, lookup, forecast_lookup

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///powsearch.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """About the PowSearch web app"""
    if request.method == "GET":
        return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    """Search database for ski resorts"""
    """Include a button to add a resort to wishlist"""

    # User reached via GET
    if request.method == "GET":
        return render_template("search.html")

    # User reached via POST
    elif request.method == "POST":

        # Get current user
        user_id = session["user_id"]

        # Clear all values in weather column from the last time this function was used and reset to null
        weatherReset_query = db.execute("UPDATE resorts SET weather = null")

        # Begin queries to execute the user's search (querying the database and calling the API)

        # Define variables that will be queried
        state_province = request.form.get("state_province")
        peak_elevation = request.form.get("peak_elevation")
        skiable_acres = request.form.get("skiable_acres")
        total_trails = request.form.get("total_trails")
        total_lifts = request.form.get("total_lifts")
        avg_snowfall = request.form.get("avg_snowfall")
        ticket_price = request.form.get("ticket_price")

        # Query database for a list of cities nearest to the ski resorts that that meet the filter criteria
        nearCity_query = db.execute("SELECT resort_id, near_city FROM resorts WHERE state_province = ? AND peak_elevation >= ? AND acres >= ? AND trails >= ? AND lifts >= ? AND avg_annual_snowfall >= ? AND ticket_price <= ?", state_province, peak_elevation, skiable_acres, total_trails, total_lifts, avg_snowfall, ticket_price)

        # Loop through the list of cities (eac row) in the table to get the forecasted weather for the nearest city to the ski resort
        for i in nearCity_query:

            # Call weather API to get the 5 day weather forecasted weather
            # forecast = forecast_lookup(nearCity_query[i])
            forecast = forecast_lookup(i["near_city"])
            print(forecast["forecast"])
            resort_id = i["resort_id"]

            # Insert the forecasted weather value (text string) into the weather column of resorts where the near_city name is equal to the city being called through the API
            # update_weather_query = db.execute("INSERT INTO resorts (weather) VALUES (?) WHERE resort_id = ?", forecast, resort_id)
            update_weather_query = db.execute("UPDATE resorts SET weather = ? WHERE resort_id = ?", forecast["forecast"], resort_id)

        # Execute final resort search query; display resort_name and weather for all results that meet search criteria
        query = db.execute("SELECT resort_name, weather FROM resorts WHERE state_province = ? AND peak_elevation >= ? AND acres >= ? AND trails >= ? AND lifts >= ? AND avg_annual_snowfall >= ? AND ticket_price <= ?", state_province, peak_elevation, skiable_acres, total_trails, total_lifts, avg_snowfall, ticket_price)

        # Render template to display query results
        if not query:
            return apology("You must like to shred in obscure locations, no results match your search", 400)

        else:
            return render_template("search_result.html", resorts=query)

# Search weather (openweathermap.org API test)
@app.route("/weather", methods=["GET", "POST"])
@login_required
def weather():
    """Search weather by city"""

    # User reached route via GET
    if request.method == "GET":
        return render_template("weather.html")

    # Ensure city name is valid
    elif request.method == "POST":
        city = lookup(request.form.get("city"))
        # city = lookup("seattle")

        # print("maxmax", city)

        if city == None:
            return apology("Choose valid city", 400)

        # If city is valid, pass data to weather_result.html
        else:
            # city = lookup("seattle")  # lookup(request.form.get("city"))
            return render_template("weather_result.html", city = city)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""

     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was chosen
        if not request.form.get("username"):
            return apology("must choose username", 400)

        # Ensure password was chosen
        elif not request.form.get("password"):
            return apology("must choose password", 400)

        # Ensure password was confirmed
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Ensure both passwords are the same
        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # Hash password and prepare to insert username and password into SQL db by defining the variables
        password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        username = request.form.get("username")

        # Query database for username to determine if username already taken
        columns = db.execute("SELECT COUNT(*) FROM users WHERE username = ?", username)
        if columns[0]["COUNT(*)"] > 0:
            return apology("username already taken", 400)

        # If username not taken, insert information into user table
        else:
            # Insert username and password into the SQL db
            db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, password)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)

            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]

     # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


@app.route("/test")
@login_required
def test():
    """test layout page"""
    if request.method == "GET":
        return render_template("test_layout.html")