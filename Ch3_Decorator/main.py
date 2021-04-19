from beverage import Beverage
from concreteDecorator import *
from createComponent import *

def run():
    beverage = Espresso()
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    print(beverage.getDescription())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
