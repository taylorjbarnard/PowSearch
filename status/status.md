# Status Report

#### Your name

Taylor Barnard

#### Your section leader's name

Shayna Sragovicz

#### Project title

PowSearch

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

I have created the shell for the website, which currently allows users to:
    1) Register for an account on the website
    2) Log in and log out using their user credentials
    3) Navigate to primary pages on the website:
        a. Search Destinations - A page that allows users to search ski resort destinations using various filtering criteria
        b. Wishlist - Displays a list of "wishlist" destinations that a user has saved.
        c. About - The homepage

#### What have you not done for your project yet?

1) Custom CSS - I have not done much CSS customization beyond playing with the font colors and the website logo.
    I tried to use bootstrap to create a drop down menu for state/province when filtering for ski resorts, but it
    isn't quite working. I currently have the code commented out and am trying to figure out how to implement it.

2) API connection - I have identified an API that seems pretty easy to use for weather data (openweathermap.org).
    To test out implementation/connecting to the API, I created a temporary page on my website that simply allows the user to search the weather for the city
    (later on I plan to use this weather data in a more robust way to enhance the Search Destination function on the website). I can't seem to return results when performing the API call.
    I think part of this has to do with parsing the API call URL incorrectly. I am still working on fixing this.

3) Search destination capability - This is currently not working. I have an HTML form that allows users to indicate their search criteria (e.g. ski resort state, average annual snowfall, etc.).
    The code is supposed to execute a SQL query and then display the results (all ski resorts that meet the search criteria) on a newly rendered HTML template - but instead I am getting a 500 error.
    I know that the SQL code is correct because I tested it separately in the phpLiteAdmin. I think the issue might be that my HTML page meant to display the SQL results doesn't properly take in/display the outcomes.
    Essentially, I need to dynamically created an HTML table that can display a varying number of rows based on the output of the SQL query.

#### What problems, if any, have you encountered?

In addition to the problems listed above, I was initially unable to upload a CSV data file to the phpLiteAdmin. I used the CS50 Ed discussion board and got assistance from a staff member to solve this problem.
