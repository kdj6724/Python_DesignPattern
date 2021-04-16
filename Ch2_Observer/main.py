# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from observer import Observer
from subject import Subject
from displayElement import DisplayElement
from weatherData import WeatherData

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: Subject):
        weatherData.registerObserver(self)

    def display(self):
        print('Current Condition: ' + self.temperature + 'F degrees and '
              + self.humidity + '%')

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

def run():
    weatherData = WeatherData
    currentDisplay = CurrentConditionsDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
