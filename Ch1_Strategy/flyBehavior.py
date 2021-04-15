from abc import *

class FlyBehavior(metaclass=ABCMeta):
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print('날고 있어요')

class FlyNoWay(FlyBehavior):
    def fly(self):
        print('저는 못 날아요')