Summative 3: Movie Review Website
================

Objectives
----------

-   Become more comfortable with Python.
-   Gain experience with Flask.
-   Learn to use SQL to interact with databases.

Overview
--------

In this project, you’ll build a movie review website. Users will be able
to register for your website and then log in using their username and
password. Once they log in, they will be able to search for movie, leave
reviews for individual movie, and see the reviews made by other people.
You’ll also use the a third-party API by OMDb, another movie review
website, to pull in ratings from a broader audience. Finally, users will
be able to query for movie details and movie reviews programmatically via
your website’s API.

Getting Started
---------------

### PostgreSQL

For this project, you’ll need to set up a PostgreSQL database to use
with our application. It’s possible to set up PostgreSQL locally on your
own computer, but for this project, we’ll use a database hosted by
[Heroku](https://www.heroku.com/), an online web hosting service.

1.  Navigate to [https://www.heroku.com/](https://www.heroku.com/), and
    create an account if you don’t already have one.
2.  On Heroku’s Dashboard, click “New” and choose “Create new app.”
3.  Give your app a name, and click “Create app.”
4.  On your app’s “Overview” page, click the “Configure Add-ons” button.
5.  In the “Add-ons” section of the page, type in and select “Heroku
    Postgres.”
6.  Choose the “Hobby Dev - Free” plan, which will give you access to a
    free PostgreSQL database that will support up to 10,000 rows of
    data. Click “Provision.”
7.  Now, click the “Heroku Postgres :: Database” link.
8.  You should now be on your database’s overview page. Click on
    “Settings”, and then “View Credentials.” This is the information
    you’ll need to log into your database. You can access the database
    via [Adminer](https://adminer.cs50.net/), filling in the server (the
    “Host” in the credentials list), your username (the “User”), your
    password, and the name of the database, all of which you can find on
    the Heroku credentials page.

Alternatively, if you install
[PostgreSQL](https://www.postgresql.org/download/) on your own computer,
you should be able to run `psql URI` on the command
line, where the `URI` is the link provided in the
Heroku credentials list.

### Python and Flask

1.  First, make sure you install a copy of
    [Python](https://www.python.org/downloads/). For this course, you
    should be using Python version 3.6 or higher.
2.  You’ll also need to install `pip`. If you
    downloaded Python from Python’s website, you likely already have
    `pip` installed (you can check by running
    `pip` in a terminal window). If you don’t have
    it installed, be sure to [install
    it](https://pip.pypa.io/en/stable/installing/) before moving on!

To try running your first Flask application:

1.  Download the `project1` distribution directory
    from
    [https://cdn.cs50.net/web/2018/spring/projects/1/project1.zip](https://cdn.cs50.net/web/2018/spring/projects/1/project1.zip)
    and unzip it.
2.  In a terminal window, navigate into your
    `project1` directory.
3.  Run `pip3 install -r requirements.txt` in your
    terminal window to make sure that all of the necessary Python
    packages (Flask and SQLAlchemy, for instance) are installed.
4.  Set the environment variable `FLASK_APP` to be
    `application.py`. On a Mac or on Linux, the
    command to do this is
    `export FLASK_APP=application.py`. On Windows,
    the command is instead
    `set FLASK_APP=application.py`. You may
    optionally want to set the environment variable
    `FLASK_DEBUG` to `1`, which
    will activate Flask’s debugger and will automatically reload your
    web application whenever you save a change to a file.
5.  Set the environment variable `DATABASE_URL` to
    be the URI of your database, which you should be able to see from
    the credentials page on Heroku.
6.  Run `flask run` to start up your Flask
    application.
7.  If you navigate to the URL provided by `flask`,
    you should see the text `"Project 1: TODO"`!

### OMDb API

OMDb (The Open Movie Database) is a RESTful webservice to obtain movie information, and we’ll be using their API
in this project to get access to their review data for individual movies.

1.  Go to [http://www.omdbapi.com/](http://www.omdbapi.com/).
2.  Navigate to
    [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)
    and apply for an API key. Select "FREE! (1,000 daily limit). Fill up your email, first name, last name and a short description of your project. Note
3.  You will be sent a verification link to activate your key via email. Click on the URL provided to activate your key.
4.  You can now use that API key to make requests to the OMDb API documented [http://www.omdbapi.com/#parameters](http://www.omdbapi.com/#parameters). In
    particular, Python code like the below

```python
import requests
res = requests.get("http://www.omdbapi.com/", params={"apikey": "<replace-with-your-own-key>", "t": "The+Godfather"})
print(res.json())
```

where `apikey` is your API key, will give you the
review and rating data for the movie with the provided movie title. In
particular, you might see something like this dictionary:

```json
{
  "Title": "The Godfather",
  "Year": "1972",
  "Rated": "R",
  "Released": "24 Mar 1972",
  "Runtime": "175 min",
  "Genre": "Crime, Drama",
  "Director": "Francis Ford Coppola",
  "Writer": "Mario Puzo (screenplay by), Francis Ford Coppola (screenplay by), Mario Puzo (based on the novel by)",
  "Actors": "Marlon Brando, Al Pacino, James Caan, Richard S. Castellano",
  "Plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
  "Language": "English, Italian, Latin",
  "Country": "USA",
  "Awards": "Won 3 Oscars. Another 24 wins & 28 nominations.",
  "Poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
  "Ratings": [
    {
      "Source": "Internet Movie Database",
      "Value": "9.2/10"
    },
    {
      "Source": "Rotten Tomatoes",
      "Value": "98%"
    },
    {
      "Source": "Metacritic",
      "Value": "100/100"
    }
  ],
  "Metascore": "100",
  "imdbRating": "9.2",
  "imdbVotes": "1,425,400",
  "imdbID": "tt0068646",
  "Type": "movie",
  "DVD": "09 Oct 2001",
  "BoxOffice": "N/A",
  "Production": "Paramount Pictures",
  "Website": "http://www.thegodfather.com",
  "Response": "True"
}
```


Requirements
------------

Alright, it’s time to actually build your web application! Here are the
requirements:

-   **Registration**: Users should be able to register for your website,
    providing (at minimum) a username and password.
-   **Login**: Users, once registered, should be able to log in to your
    website with their username and password.
-   **Logout**: Logged in users should be able to log out of the site.
-   **Import**: Provided for you in this project is a file called
    `movies.csv`, which is a spreadsheet in CSV
    format of 250 different movies. Each one has an movie title, release year, runtime, IMDB ID, and
    IMDB rating. In a Python file called
    `import.py` separate from your web application,
    write a program that will take the movies and import them into your
    PostgreSQL database. You will first need to decide what table(s) to
    create, what columns those tables should have, and how they should
    relate to one another. Run this program by running
    `python3 import.py` to import the movies into
    your database, and submit this program with the rest of your project
    code.
-   **Search**: Once a user has logged in, they should be taken to a
    page where they can search for a movie. Users should be able to type
    in the title of a movie, IMDB ID, or Year of Release. After performing the search, your website should display a
    list of possible matching results, or some sort of message if there
    were no matches. If the user typed in only part of a title, your search page should find matches for those as well!
-   **Movie Page**: When users click on a movie from the results of the
    search page, they should be taken to a movie page, with details about
    the movie: its title,  IMDB id, year of release, runtime, IMDB rating, and any
    reviews that users have left for the movie on your website.
-   **Review Submission**: On the movie page, users should be able to
    submit a review: consisting of a rating on a scale of 1 to 10, as
    well as a text component to the review where the user can write
    their opinion about a movie. Users should not be able to submit
    multiple reviews for the same movie.
-   **OMDB Data**: On your movie page, you could also
    display (if available) the movie plot, genre, director, actors and poster, or any other relevant.
-   **API Access**: If users make a GET request to your website’s
    `/api/<imdb_id>` route, where
    `<imdb_id>` is the IMDB id, your website should
    return a JSON response containing the movie’s title, year of release,
    imdb id, director, actors, imdb_rating, review count, and average score. The
    resulting JSON should follow the format:

```python
{
    "title": "The Godfather",
    "year": 1972,
    "imdb_id": "tt0068646",
    "director": "Francis Ford Coppola",
    "actors": "Marlon Brando, Al Pacino, James Caan, Richard S. Castellano",
    "imdb_rating": 9.2
    "review_count": 28,
    "average_score": 9.8,
}
```

If the requested IMDB id isn’t in your database, your website should
return a 404 error.

-   You should be using raw SQL commands (as via SQLAlchemy’s
    `execute` method) in order to make database
    queries. You should not use the SQLAlchemy ORM (if familiar with it)
    for this project.
-   In `README.md`, include a short writeup
    describing your project, what’s contained in each file, and
    (optionally) any other additional information the staff should know
    about your project.
-   If you’ve added any Python packages that need to be installed in
    order to run your web application, be sure to add them to
    `requirements.txt`!

Beyond these requirements, the design, look, and feel of the website are
up to you! You’re also welcome to add additional features to your
website, so long as you meet the requirements laid out in the above
specification!

Hints
-----

-   At minimum, you’ll probably want at least one table to keep track of
    users, one table to keep track of movies, and one table to keep track
    of reviews. But you’re not limited to just these tables, if you
    think others would be helpful!
-   In terms of how to “log a user in,” recall that you can store
    information inside of the `session`, which can
    store different values for different users. In particular, if each
    user has an `id`, then you could store that
    `id` in the session (e.g., in
    `session["user_id"]`) to keep track of which
    user is currently logged in.

FAQs
----

### For the API, do the JSON keys need to be in order?

Any order is fine!

### `AttributeError: 'NoneType' object has no attribute '_instantiate_plugins'`

Make sure that you’ve set your `DATABASE_URL`
environment variable before running `flask run`!

How to Submit
-------------

1.  Submit using [Summative Submission Link](https://tinyurl.com/2019-y3cep-summative).
2.  [Record a 1- to 5-minute
    screencast](https://www.howtogeek.com/205742/how-to-record-your-windows-mac-linux-android-or-ios-screen/)
    in which you demonstrate your app’s functionality and/or walk
    viewers through your code. [Upload that video to
    YouTube](https://www.youtube.com/upload) (as unlisted or public, but
    not private) or somewhere else.
