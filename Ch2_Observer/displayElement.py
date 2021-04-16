from abc import *

class DisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass