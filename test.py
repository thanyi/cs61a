
class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year



class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10
    def dime_print(self):
        return self.cents