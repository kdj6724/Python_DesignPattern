from observer import Observer
from subject import Subject

class WeatherData(Subject):
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObserver()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()