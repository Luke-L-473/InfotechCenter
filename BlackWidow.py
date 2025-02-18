import random  # Importing the random module to generate random values
from time import sleep  # Importing the sleep function to add pauses

# Printing an initial message indicating the developer and program
print("\n***********************************\n\nGasoline Branch - Developer: Luke Lenzinger\n")

# Function to simulate a random gas level reading
def gasLevelGauge():
    # Randomly choose a gas level from the available options
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

# Function to simulate a random gas station name
def gasStations():
    # Randomly choose a gas station name from a predefined list
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "7/11", "Sam's Club", "Buc-ee's"])

# Function to generate and display a gas level alert based on the current gas level
def gasLevelAlert():
    g = gasLevelGauge()  # Call gasLevelGauge() to get a random gas level
    if g == "Empty":  # If the gas level is "Empty"
        # Display a warning message and simulate calling AAA
        print("**** WARNING - YOU ARE OUT OF GAS ****\nCalling AAA...\n")
    elif g in ["Low", "Quarter Tank"]:  # If the gas level is "Low" or "Quarter Tank"
        # Display the current gas level and the closest gas station, including a random distance (1 to 25 miles if "Low", 1 to 50 miles if "Quarter Tank")
        print(f"Your gas tank is {g}. Closest station: {gasStations()}, {round(random.uniform(1, 25 if g == 'Low' else 50), 1)} miles away.\n")
        sleep(1.25)  # Pause for 1.25 seconds before proceeding
    else:  # If the gas level is "Half Tank", "Three Quarter Tank", or "Full Tank"
        # Display a message indicating the user is good to go with enough fuel
        print(f"Your gas tank is {g}. You're good to go!\n")

# Call the gasLevelAlert function to run the alert system
gasLevelAlert()
