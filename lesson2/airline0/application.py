import os

import psycopg2
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
#DATABASE_URL = "postgresql+psycopg2://usygtmsgbejhsu:b06b1b8bafa4f4b194d415955b47a30ec34672fb44bbf70e490a5da45e6384ad@ec2-174-129-10-235.compute-1.amazonaws.com:5432/d1ceb2a8b68h58"
#engine = create_engine(DATABASE_URL)
engine = create_engine(os.getenv("DATABASE_URL"))
#engine = psycopg2.connect(DATABASE_URL, sslmode='require')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)
    # try:
    #
    # except Exception as e:
    #     print(e)
    # #return "Nothing"

@app.route("/showall")
def showall():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information.
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
            {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")
