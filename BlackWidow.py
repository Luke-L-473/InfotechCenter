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


print("\n*********************************\n\nWeather Branch - Developer: Luke Lenzinger")
def vehicle_response_system(w):
    d, s = {"snowy": (30, 45), "blizzard": (60, 35), "icy": (60, 45), "rainy": (15, 55), "windy": (10, 60)}.get(w, (0, 70))
    print(f"\nThe National Weather Service {'updated your alarm by ' + str(d) + ' minutes due to ' + w if d else 'calls for ' + w + ' skies outside. Drive safe!'}")
    time.sleep(1)
    print(f"VRS engaged, max speed {s} MPH.")
vehicle_response_system(random.choice(["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]))
