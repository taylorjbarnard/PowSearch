import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(city):
    """Lookup current weather for a city"""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote_plus(city)}&appid={api_key}&units=imperial"

        response = requests.get(url)

        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        city = response.json()
        return {
            "name": city["name"],
            "temperature": city["main"]["temp"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def forecast_lookup(city):
    """Lookup future weather forecast for a city"""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={urllib.parse.quote_plus(city)}&appid={api_key}"

        response = requests.get(url)

        response.raise_for_status()
    except requests.RequestException:
        print("error1")
        return None

    # Parse response
    try:
        city = response.json()
        return {
            "forecast": city["list"][0]["weather"][0]["description"]
            # "forecast": city["city"]["name"]
        }
    except (KeyError, TypeError, ValueError):
        print("error2")
        return None

