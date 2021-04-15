from abc import *

class QuackBehavior(metaclass=ABCMeta):
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print('꽥')

class MuteQuack(QuackBehavior):
    def quack(self):
        print('조용')

class Squack(QuackBehavior):
    def quack(self):
        print('삑')