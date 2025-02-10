print("\n*********************************\n")

print("Weather Branch - Developer: Luke Lenzinger\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine weather
def weather():
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny",]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " of the forecasted", weatherAlert, "weather condiditons.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " of the forecasted", weatherAlert, ".")
        
vehicleResponseSystem()