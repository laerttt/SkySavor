from flask import Flask, render_template
import json
from static.Objects.BookedSegment import Flight, Country
from static.Objects.Client import Traveller

app = Flask(__name__)
LEVEL_POINTS={

    1:300,
    2:600,
    3:800,
    4:1300,
    5: 2000,
    6: 3000,
    }
LEVEL_POINTS_LENGTH=8
@app.route("/")
def landingPage():
    France = Country("Europe", "France", "Charles de Gaulle Airport")
    Japan = Country("Asia", "Japan", "Narita International Airport")
    USA = Country("North America", "USA", "JFK International Airport")

    flight_data = [
        Flight(France, Japan, "AA124", "2023-10-26", "AA", "2023-10-26 08:00", "2023-10-26 10:30", "BUSINESS",
                      500.0, 12.0, 300),
        Flight(USA, France, "UA456", "2023-10-27", "UA", "2023-10-27 09:00", "2023-10-27 11:30",
                      "PREMIUM_ECONOMY", 400.0, 11.0, 232),
        Flight(Japan, USA, "UA457", "2023-10-28", "UA", "2023-10-28 09:00", "2023-10-28 11:30", "ECONOMY",
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
        flights= flight_data
    )
    # variables for roadmap trophies
    currLevel = findCurrLevel(traveller)
    nextLevelPoints = LEVEL_POINTS[currLevel + 1] - traveller.km
    LevelPoints = LEVEL_POINTS[currLevel]

    #json for map
    json=obj_to_json(traveller)

    print(json)
    print(currLevel)
    print(nextLevelPoints)
    print(LevelPoints)


    # currLevel (self explanatory)
    # nextLevelPoints dictionary containing diff level points
    # levelPoints specific level points

    return render_template("index.html",flights=traveller.flights,json=json,currLevel=currLevel, nextLevelPoints=nextLevelPoints, levelPoints=LevelPoints, tokens=20, firstname=traveller.firstName, lastname=traveller.lastName, km=traveller.km)
def findCurrLevel(obj):
    for i in range(1,LEVEL_POINTS_LENGTH):
        if obj.km > LEVEL_POINTS[i]:
            None
        elif obj.km==LEVEL_POINTS[i]:
            return i
        elif obj.km < LEVEL_POINTS[i]:
            return i

@app.route("/Shop")
def shopPage():
    return render_template("shop.html")

FLASK_ENV="development"
FLASK_APP="main.py"
def obj_to_json(obj):
    list=obj.visitedCountries
    return json.dumps(list)



if __name__ == '__main__':
    app.run(debug=True)