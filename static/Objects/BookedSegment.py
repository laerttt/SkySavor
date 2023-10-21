from enum import Enum
from pydantic import BaseModel
import re
from datetime import datetime


flightNumber_PATTERN=r"^[A-Z]{2}[0-9]{4}$"
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
class Flight(BaseModel):

    origin: str
    destination: str
    distance: int
    flightNumber: str
    flightDate: str  # datetime
    airlineCode: str
    departureDate: str  # na duhet datetime
    arrivalDate: str  # datetime
    bookingClass: BookingClass
    price: float
    taxPercentage: float
    def __init__(self, origin, destination, flightNumber, flightDate, airlineCode, departureDate, arrivalDate, bookingClass, price, taxPercentage):
        self.origin = origin
        self.destination = destination
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

