from abc import *
from observer import Observer

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def registerObserver(self, observer: Observer):
        pass

    @abstractmethod
    def removeObserver(self, observer: Observer):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass