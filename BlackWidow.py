import random
from time import sleep

print("\n*********************************\n")
print("Weather Branch - Developer: Luke Lenzinger")

# Weather function to determine weather
def weather():
    return random.choice(["snowy", "blizzard", "icy", "rainy", "windy", "sunny"])

# Optimized Vehicle Response System
def vehicle_response_system(weather_condition):
    weather_data = {
        "snowy": (30, 45),
        "blizzard": (60, 35),
        "icy": (60, 45),
        "rainy": (15, 55),
        "windy": (10, 60),
        "sunny": (0, 70)
    }

    delay, speed_limit = weather_data.get(weather_condition, (0, 70))

    if delay:
        print(f"\nThe National Weather Service has updated your alarm by {delay} minutes due to {weather_condition} conditions.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_condition} skies outside. Drive safe!")

    sleep(1)
    print(f"VRS has been engaged, allowing a maximum speed of {speed_limit} MPH.")

# Run the system
current_weather = weather()
vehicle_response_system(current_weather)
