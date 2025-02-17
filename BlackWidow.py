print("\n***********************************\n")
print("Gasoline Branch - Developer: Luke Lenzinger\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "7/11", "Sam's Club", "Buc-ee's"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        sleep(1.25)
        print("Calling AAA\n")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station.\n")
        sleep(1.25)
        print("The cosest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.\n")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a Quarter Tank full, checking GPS for the closest gas station.\n")
        sleep(1.25)
        print("The cosest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.\n")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is on a Half of a Tank, which is plenty to get to your destination!\n")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is Three Quarters of a Tank full, which is more than a enough to get to your destination!\n")
    else:
        print("You have a Full Tank of gas, which is more than enough to get you to your destination!\n")

gasLevelAlert()        