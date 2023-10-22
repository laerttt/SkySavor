from flask import Flask, render_template, request,redirect,url_for
import json
from static.Objects.BookedSegment import Flight, Country
from static.Objects.Bundle import Bundle
from static.Objects.Client import Traveller
import static.Controllers.kodiqr as kodiqr

app = Flask(__name__)


#NECCESARY GLOBAL DATA TO SIMULATE LOG IN STATUS
France = Country("France", "Europe", "CGA")
Japan = Country("Japan", "Asia", "MIA")
USA = Country("USA", "North America", "JFK")

flight_data = [
    Flight(France, Japan, "AA124", "2023-10-26", "AA", "2023-10-26 08:00", "2023-10-26 10:30", "BUSINESS",
           500.0, 12.0, 800),
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
    flights=flight_data
)
bundle_data = [Bundle(False, 20, "Enjoy the best quality champagne, mixed with the excellent service of our staff. ",
                      "Buy Dom Perignon in next flight", "/static/images/dom-perignon.jpg", "bundles3"),
               Bundle(False, 4, "You have the opportunity to surf the net freely and without any additional fees. ",
                      "Free internet for the whole flight",
                      "/static/images/wifi.png", "bundles2"),
               Bundle(False, 6, "You can be the first to check in and board without worrying about long lines",
                      "Check-in and boarding priority",
                      "/static/images/boarding.png", "bundle1")]

trophy_bundle = [Bundle(False, 0, "Bundle 1 Description", "troph 1", "bundle1.jpg", "bundles3"),
               Bundle(False, 0, "Bundle 2 Description", "troph 2",
                      "bundle2.jpg", "bundles2"),
               Bundle(False, 0, "Bundle 3 Description", "troph 3",
                      "bundle3.jpg", "bundle1"),
                 Bundle(False, 0, "Bundle 1 Description", "troph 1", "bundle1.jpg", "bundles3"),
                 Bundle(False, 0, "Bundle 2 Description", "troph 2",
                        "bundle2.jpg", "bundles2"),
                 Bundle(False, 0, "Bundle 3 Description", "troph 3",
                        "bundle3.jpg", "bundle1"),
                 ]

#END OF GLOBAL DATA

LEVEL_POINTS={
    0:50,
    1:300,
    2:600,
    3:800,
    4:1300,
    5: 2000,
    6: 3000,
    }

LEVEL_POINTS_LENGTH=8
CurrTokens=0
@app.route("/")
def landingPage():





    # variables for roadmap trophies
    currLevel = findCurrLevel(traveller)
    nextLevelPoints = LEVEL_POINTS[currLevel + 1] - traveller.km
    LevelPoints = LEVEL_POINTS[currLevel]
    map_data={}
    for flight in flight_data:
        map_data[flight.origin.Name] = flight.origin.continent
        map_data[flight.destination.Name] = flight.destination.continent

    print(map_data)
    print(traveller.tokens)

    # currLevel (self explanatory)
    # nextLevelPoints dictionary containing diff level points
    # levelPoints specific level points

    return render_template("index.html",flights=traveller.flights,json=map_data,currLevel=currLevel, nextLevelPoints=nextLevelPoints, levelPoints=LevelPoints, tokens=traveller.tokens, firstname=traveller.firstName, lastname=traveller.lastName, km=traveller.km)


def findCurrLevel(obj):
    for i in range(1,LEVEL_POINTS_LENGTH):
        if obj.km > LEVEL_POINTS[i]:
            None
        elif obj.km==LEVEL_POINTS[i]:
            return i
        elif obj.km < LEVEL_POINTS[i]:
            return i

@app.route('/Shop', methods=['GET', 'POST'])
def shopPage():
    global CurrTokens

    if request.method == "POST":
      for bundle in bundle_data:
          if bundle.name in request.form:
             if traveller.tokens<bundle.price:
                 None
             else:
              print("a futet")
              bundle.redeemed=True
              traveller.tokens=traveller.tokens-bundle.price
              landingPage()

    return render_template('shop.html',bundles=bundle_data)

@app.route("/inventory", methods=['GET', 'POST'])
def inventory():
    valid_bundle=[]
    TrophPlace=findCurrLevel(traveller)
    print(TrophPlace)
    for bundle in bundle_data:
        print(bundle._picture)
        if bundle.redeemed==True:
            print(1001)
            valid_bundle.append(bundle)
    for key in range(0,LEVEL_POINTS_LENGTH):
       if traveller.km>LEVEL_POINTS[key]:
           trophy_bundle[key].redeemed==True
           valid_bundle.append(trophy_bundle[key])
       else: break

    if request.method == 'POST':
        kodiqr.generate("https://github.com/laerttt/SkySavor", "qrCode")
        path = "static/QR/qrCode.png"
        return render_template("inventory.html", bundles=valid_bundle, path=path)
    return render_template("inventory.html",bundles=valid_bundle)





FLASK_ENV="development"
FLASK_APP="main.py"
# def obj_to_json(obj):
#     return json.dumps(obj)



if __name__ == '__main__':
    app.run(debug=True)