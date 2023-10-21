
class Traveller():
    flights:list
    visitedCountries: list
    km: int
    firstName: str
    lastName: str
    middleName: str = None
    salutation: str
    gender: str
    passengerType: str
    frequentFlyerNumber: str = None
    linkedUserAccount: str
    currLevel:int
    tokens: int

   #tokens and visited not added to innit for later to do
    def __init__(self, firstName, lastName, middleName=None, salutation=None,
                 gender=None, passengerType=None,
                 frequentFlyerNumber=None , linkedUserAccount=None,flights=None):
        self._firstName = firstName
        self._lastName = lastName
        self._middleName = middleName
        self._salutation = salutation
        self._gender = gender
        self._passengerType = passengerType
        self._frequentFlyerNumber = frequentFlyerNumber
        self._linkedUserAccount = linkedUserAccount
        self._flights = flights
        self._km=0
        self._visitedCountries = []
        self._tokens = 0
        for flight in self._flights:
                self._km=self._km+flight.distance
                if flight.bookingClass == "ECONOMY":
                    self._tokens= self._tokens+1
                elif flight.bookingClass == "PREMIUM_ECONOMY":
                    self._tokens= self._tokens+2
                elif flight.bookingClass == "BUSINESS":
                    self._tokens= self._tokens+3
                elif flight.bookingClass == "FIRST":
                    self._tokens= self._tokens+4

                if flight.origin.Name in self._visitedCountries:
                    None
                else: self._visitedCountries.append(flight.origin.Name)

                if flight.destination.Name in self._visitedCountries:
                    None
                else:  self._visitedCountries.append(flight.destination.Name)

        

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        if isinstance(value, str):
            self._firstName = value
        else:
            raise ValueError("First name must be a string")

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        if isinstance(value, str):
            self._lastName = value
        else:
            raise ValueError("Last name must be a string")

    @property
    def middleName(self):
        return self._middleName

    @middleName.setter
    def middleName(self, value):
        if value is None or isinstance(value, str):
            self._middleName = value
        else:
            raise ValueError("Middle name must be a string or None")

    @property
    def salutation(self):
        return self._salutation

    @salutation.setter
    def salutation(self, value):
        if value is None or isinstance(value, str):
            self._salutation = value
        else:
            raise ValueError("Salutation must be a string or None")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value is None or isinstance(value, str):
            self._gender = value
        else:
            raise ValueError("Gender must be a string or None")

    @property
    def passengerType(self):
        return self._passengerType

    @passengerType.setter
    def passengerType(self, value):
        if value is None or isinstance(value, str):
            self._passengerType = value
        else:
            raise ValueError("Passenger type must be a string or None")

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        # You may need to implement more specific validation for the 'document' attribute based on the actual schema
        if value is None or isinstance(value, dict):
            self._document = value
        else:
            raise ValueError("Document must be a dictionary or None")

    @property
    def frequentFlyerNumber(self):
        return self._frequentFlyerNumber

    @frequentFlyerNumber.setter
    def frequentFlyerNumber(self, value):
        if value is None or isinstance(value, str):
            self._frequentFlyerNumber = value
        else:
            raise ValueError("Frequent flyer number must be a string or None")

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if value is None or isinstance(value, dict):
            self._contact = value
        else:
            raise ValueError("Contact must be a dictionary or None")

    @property
    def linkedUserAccount(self):
        return self._linkedUserAccount

    @linkedUserAccount.setter
    def linkedUserAccount(self, value):
        if isinstance(value, str):
            self._linkedUserAccount = value
        else:
            raise ValueError("Linked user account must be a string")
    @property
    def flights(self):
        return self._flights
    @property
    def visitedCountries(self):
        return self._visitedCountries

    # Setter for visitedCountries
    @visitedCountries.setter
    def visitedCountries(self, countries):
        if isinstance(countries, list):
            self._visitedCountries = countries
        else:
            raise ValueError("visitedCountries must be a list")

    # Getter for km
    @property
    def km(self):
        return self._km

    # Setter for km
    @km.setter
    def km(self, kilometers):
        if isinstance(kilometers, int):
            self._km = kilometers
        else:
            raise ValueError("km must be an integer")

    @property
    def tokens(self):
        return self._tokens

    @tokens.setter
    def tokens(self, new_tokens):
        if isinstance(new_tokens, int):
            self._tokens = new_tokens
        else:
            raise ValueError("Token must be an integer")


