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

print(gasLevelGauge())
print(gasStations())