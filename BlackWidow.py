print("\n*********************************\n")

print("Weather Branch - Developer: Luke Lenzinger\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine weather
def weather():
    weatherForecastList = ["snowing", "blizzard", "icy", "rain", "windy", "sunny",]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

print(weather())