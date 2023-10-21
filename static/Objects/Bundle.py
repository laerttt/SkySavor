class Bundle:
    def __init__(self, redeemed: bool, price: int, description: str):
        self._redeemed = redeemed
        self._price = price
        self._description = description

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


