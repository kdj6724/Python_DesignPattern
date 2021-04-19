from abc import *

class Beverage(metaclass=ABCMeta):
    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass