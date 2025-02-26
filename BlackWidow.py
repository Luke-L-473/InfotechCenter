# Import necessary libraries
import sys  # Used for controlling output display
import time  # Used for adding delays
import random, time

# Define ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Reset color to default

# Display developer information in cyan
print(CYAN + "Welcome Branch - Developer: Luke Lenzinger\n" + RESET)

# Display the main system message in yellow
print(YELLOW + "Welcome to InfoTechCenter V1.0\n" + RESET)

# Initialize variables
x = 0  # Counter for the loop
ellipsis = 0  # Controls the number of dots displayed

# Loop to create a boot-up animation effect
while x != 20:
    x += 1  # Increment counter
    
    # Create a loading message with increasing dots in blue
    message = (BLUE + "Infotech Center System Booting" + "." * ellipsis + RESET)
    
    ellipsis += 1  # Increment ellipsis count for dot animation
    
    # Overwrite the previous line with the new message
    sys.stdout.write("\r" + message)
    
    # Pause to create the animation effect
    time.sleep(.5)
    
    # Reset the ellipsis count after reaching 3 dots
    if ellipsis == 4:
        ellipsis = 0
    
    # After 20 iterations, display the final message in green
    if x == 20:
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted" + RESET)

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

print("\n*********************************\n\nWeather Branch - Developer: Luke Lenzinger")
def vehicle_response_system(w):
    d, s = {"snowy": (30, 45), "blizzard": (60, 35), "icy": (60, 45), "rainy": (15, 55), "windy": (10, 60)}.get(w, (0, 70))
    print(f"\nThe National Weather Service {'updated your alarm by ' + str(d) + ' minutes due to ' + w if d else 'calls for ' + w + ' skies outside. Drive safe!'}")
    time.sleep(1)
    print(f"VRS engaged, max speed {s} MPH.")
vehicle_response_system(random.choice(["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]))