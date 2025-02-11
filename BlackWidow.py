import random, time
print("\n*********************************\nWeather Branch - Developer: Luke Lenzinger")
def vehicle_response_system(w):
    d, s = {"snowy": (30, 45), "blizzard": (60, 35), "icy": (60, 45), "rainy": (15, 55), "windy": (10, 60)}.get(w, (0, 70))
    print(f"\nThe National Weather Service {'updated your alarm by ' + str(d) + ' minutes due to ' + w if d else 'calls for ' + w + ' skies outside. Drive safe!'}")
    time.sleep(1)
    print(f"VRS engaged, max speed {s} MPH.")
vehicle_response_system(random.choice(["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]))