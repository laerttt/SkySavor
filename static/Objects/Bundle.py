class Bundle:
    def __init__(self, redeemed: bool, price: int, description: str, header: str, picture: str, name:str):
        self._redeemed = redeemed
        self._price = price
        self._description = description
        self._header = header
        self._picture = picture
        self._name=name

    @property
    def redeemed(self):
        return self._redeemed

    @redeemed.setter
    def redeemed(self, value):
        if isinstance(value, bool):
            self._redeemed = value
        else:
            raise ValueError("Redeemed must be a boolean")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a boolean")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, int):
            self._price = value
        else:
            raise ValueError("Price must be an integer")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self._description = value
        else:
            raise ValueError("Description must be a string")

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, str):
            self._header = value
        else:
            raise ValueError("Header must be a string")

    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        if isinstance(value, str):
            self._picture = value
        else:
            raise ValueError("Picture must be a string")


