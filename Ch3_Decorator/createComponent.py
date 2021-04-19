from beverage import Beverage

class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'HouseBlend'

    def cost(self):
        return 0.89

class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'DarkRoast'

    def cost(self):
        return 0.99

class Decaf(Beverage):
    def __init__(self):
        self.description = 'Decaf'

    def cost(self):
        return 1.05