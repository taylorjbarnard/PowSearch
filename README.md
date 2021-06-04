## OVERVIEW

This...is PowSearch.

For a video walk-through of PowSearch, please visit: https://youtu.be/jhkPJ2Z8K5M

PowSearch (i.e. "powder search") is a web app that allows skiers and snowboarders to search North American ski resorts. Users can search for
resorts that meet their search criteria. Upon returning their search results, users can also see the descriptive, average
5-day weather forecast for the city closest to each ski resort. Lastly, users can use a general weather search feature
to look up the current temperature in any city. Please see DESIGN.md for a technical overview of the website development.
See DESIGN.md section "FILE DIRECTORY FOR POWSEARCH PROJECT" for a list of/description of each file in the project .zip file.

Although simple by real-world standards, I am incredibly proud of this website. It has given me the opportunity to test many of the skills I learned in CS50.
I took this class knowing that it would be my last formal opportunity to learn the basics of computer programming, something I have wanted to do for some time.
I have not been disappointed. I hope you enjoy PowSearch!

## RUNNING THE APPLICATION

PowSearch exists in the CS50 cloud9 IDE

 1) ADD PROJECT FILES TO CS50 IDE
    a) Retreive the proejct files .zip from gradescope add drag/drop them into your cloud9/CS50 environment
    b) In your terminal, CD into the folder that the files exist in

 2) CONNECT TO THE API
    a) PowSearch uses a free weather data API from openweathermap.org. Specifically, it uses two different API calls (more info below)
    b) To enable the API functionality on PowSearch, type into your terminal (excluding the quotations) "export API_KEY=62fd0f6f4d938652ab8198ca09401db2"
    c) Click enter

 3) RUN THE APPLICATION
    a) In your terminal, type (excluding the quotations) "flask run"
    b) Click enter
    c) Within the terminal you will see "* Running on _______" Where the blank is a hyperlink to the PowSearch web app
    d) Click the hyperlink and select "Open" from the menu

## REGISTER FOR A POWSEARCH ACCOUNT

 1) FIND REGISTRATION PAGE
    a) Upon enter the PowSearch website, you will be automatically directed to the login page
    b) Since you do not have a log-in, you will need to register for an account
    c) Click "register" in the top right corner, or the "register here" link beneath the login button

 2) REGISTER
    a) Fill out the form, choosing a unique username and password and then confirm your password
    b) Click "register"
    c) You will receive error messages if any fields are left blank, if your username is taken, or if you passwords do not match

## NAVIGATING POWSEARCH

Once you have registered, you will be automatically logged in and directed to the index (or "about") page.

 1) WEBSITE FEATURES
    a) PowSearch title - you can click the title in the top-left corner at any point to redirect to the "about" page
    b) About page - you can click "about" in the navbar to redirect at any point to the "about" page
    c) Destinations page -you can cick this page in the navbar to redirect at any point to the main search feature of the website
    d) Weather page - you can click this page in the navbar to redirect at any point to the current weather search feature of the website
    e) Log out - you can click "logout" in the navbar to be redirected to the login page, and from there you can navigate to the "register page"
    f) Footer information - Each page contains a footer which links to the original ski resort data source, as well as the API.
    g) Error messages are displayed, featuring a skier in a dinosaur cosutume, whenever you perform an action that isn't allowed.

 2) SEARCHING SKI DESTINATIONS
    a) Click "Destinations" in the navigation menu
    b) Fill out each field in the search menu - you are required to enter a value for each field
    c) When filling out the fields, you can run the following test search
        State/Province: Utah
        Minimum Elevation: 4000
        Minimum Acres: 500
        Minimum trails: 20
        Minimum Lifts: 6
        Minimum Snowfall: 300
        Maximum Ticket Price: 200
    d) This will redirect you to a page displaying the resorts that meet your criteria and the typical weather over the next 5 days (e.g. "overcast" or "snow")

 3) SEARCHING THE CURRENT WEATHER
    This features allows users to search current weather in any city. This is especially useful if you are spending multiple days at a resort, are already there, and want to check the weather before you head out
    a) Click "Weather" in the main navigation bar
    b) Enter the name of a city you want to search (this is not case-sensitive)
    c) View the current temperature (you will receive an error message if your city isn't valid)

## SUMMARY

Thank you! This...was PowSearch.