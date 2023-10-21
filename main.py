from flask import Flask, render_template
import json
from static.Objects.BookedSegment import Flight, Country
from static.Objects.Client import Traveller

app = Flask(__name__)

@app.route("/")
def landingPage():



    flight_data = [
        Flight("LAX", "JFK", "AA124", "2023-10-26", "AA", "2023-10-26 08:00", "2023-10-26 10:30", "BUSINESS",
                      500.0, 12.0, 300),
        Flight("SFO", "ORD", "UA456", "2023-10-27", "UA", "2023-10-27 09:00", "2023-10-27 11:30",
                      "PREMIUM_ECONOMY", 400.0, 11.0, 232),
        Flight("ORD", "SFO", "UA457", "2023-10-28", "UA", "2023-10-28 09:00", "2023-10-28 11:30", "ECONOMY",
                      350.0, 10.5, 123)
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
    Albania=Country("Albania","Europe")
    json=obj_to_json(traveller.visitedCountries)
    return render_template("index.html",flights=traveller.flights,json=json)



@app.route("/Shop")
def shopPage():
    return render_template("shop.html")

FLASK_ENV="development"
FLASK_APP="main.py"
def obj_to_json(obj):
    return json.dumps(obj)



if __name__ == '__main__':
    app.run(debug=True)