print("\n*********************************\n")

print("Weather Branch - Developer: Luke Lenzinger")

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
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " of the forecasted", weatherAlert, "conditions.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 35MPH")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " of the forecasted", weatherAlert, "road conditions.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 45MPH")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated your alarm by 15 minutes because"
              " of the forecasted", weatherAlert, "weather.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55MPH")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 10 minutes because"
              " of the forecasted", weatherAlert, "conditions.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 60MPH")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 70MPH")
        
vehicleResponseSystem()