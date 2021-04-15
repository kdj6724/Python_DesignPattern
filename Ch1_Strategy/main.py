from duck import Duck
from flyBehavior import FlyWithWings
from quackBehavior import Quack

class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print('저는 물오리 입니다.')

def run():
    mallard = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
