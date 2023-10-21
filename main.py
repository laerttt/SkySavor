from flask import Flask, render_template

from static.Objects.BookedSegment import Flight
from static.Objects.Client import Traveller

app = Flask(__name__)

@app.route("/")
def landingPage():
    flight_data = [
        Flight("JFK", "LAX", "AA123", "2023-10-25", "AA", "2023-10-25 08:00", "2023-10-25 10:30", "ECONOMY",
                      300.0, 10.0),
        Flight("LAX", "JFK", "AA124", "2023-10-26", "AA", "2023-10-26 08:00", "2023-10-26 10:30", "BUSINESS",
                      500.0, 12.0),
        Flight("SFO", "ORD", "UA456", "2023-10-27", "UA", "2023-10-27 09:00", "2023-10-27 11:30",
                      "PREMIUM_ECONOMY", 400.0, 11.0),
        Flight("ORD", "SFO", "UA457", "2023-10-28", "UA", "2023-10-28 09:00", "2023-10-28 11:30", "ECONOMY",
                      350.0, 10.5)
    ]
    traveller = Traveller(
        firstName="John",
        lastName="Doe",
        middleName="M.",
        salutation="Mr.",
        gender="Male",
        passengerType="Adult",
        frequentFlyerNumber="FF123",
        linkedUserAccount="user123",
        flights=flight_data
    )
    return render_template("base.html",flights=traveller.flights)
@app.route("/Shop")
def shopPage():
    return render_template(".html")

FLASK_ENV="development"
FLASK_APP="main.py"


if __name__ == '__main__':
    app.run(debug=True)