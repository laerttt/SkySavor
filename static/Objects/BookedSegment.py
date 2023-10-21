from enum import Enum
import re
from datetime import datetime


flightNumber_PATTERN=r"^[A-Z]{2}[0-9]{3}$"
airlineCode_PATTERN=r"^[A-Z]{2}$"

class BookingClass(Enum):
    ECONOMY = 'ECONOMY'
    PREMIUM_ECONOMY = 'PREMIUM_ECONOMY'
    BUSINESS = 'BUSINESS'
    FIRST = 'FIRST'
class TicketStatus(Enum):
    ACTIVE = 'ACTIVE'
    CANCELED = 'CANCELED'
    REFUNDED = 'REFUNDED'
class Continent(Enum):
    AFRICA = "Africa"
    ANTARCTICA = "Antarctica"
    ASIA = "Asia"
    EUROPE = "Europe"
    NORTH_AMERICA = "North America"
    OCEANIA = "Oceania"
    SOUTH_AMERICA = "South America"

class Country:
    Continent:Continent
    Name:str
    Aeroport:str

    @property
    def Continent(self):
        return self._continent

    @Continent.setter
    def Continent(self, continent):
        self._continent = continent

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    @property
    def Aeroport(self):
        return self._aeroport

    @Aeroport.setter
    def Aeroport(self, aeroport):
        self._aeroport = aeroport
    def __init__(self, name, continent,Aeroport):
        self.Name = name
        self.continent = continent
        self.Aeroport=Aeroport

class Flight():

    origin: Country
    destination: Country
    distance: int
    flightNumber: str
    flightDate: str  # datetime
    airlineCode: str
    departureDate: str  # na duhet datetime
    arrivalDate: str  # datetime
    bookingClass: BookingClass
    price: float
    taxPercentage: float

    def __init__(self, origin, destination, flightNumber, flightDate, airlineCode, departureDate, arrivalDate, bookingClass, price, taxPercentage, distance):
        self.distance = int(distance)
        self.origin = origin
        self.destination = destination
        print(flightNumber)
        if re.match(flightNumber_PATTERN, flightNumber):
            
            self.flightNumber = flightNumber
        else:
            raise ValueError("Flight Number incorrect")
        self.flightNumber = flightNumber
        self.flightDate = flightDate
        if re.match(airlineCode_PATTERN, airlineCode):
            self.airlineCode = airlineCode
        else:
            raise ValueError("AirLine Code incorrect")
        self.departureDate = departureDate
        self.arrivalDate = arrivalDate
        self.bookingClass = bookingClass
        self.price = price
        self.taxPercentage = taxPercentage

    @property
    def getDistance(self):
        return self.distance


