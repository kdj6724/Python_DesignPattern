from abc import *
from flyBehavior import *
from quackBehavior import *

class Duck(metaclass=ABCMeta):
    def __init__(self):
        self.flyBehavior = FlyBehavior
        self.quackBehavior = QuackBehavior

    def display(self):
        pass

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    def swim(self):
        print('모든 오리는 물에 뜹니다. 까짜 오리도 뜨죠')
