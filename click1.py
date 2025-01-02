import pyautogui
import json
import time

# Path to the JSON file with coordinates
coordinates_file = "coordinates.json"

# Load coordinates from the JSON file
try:
    with open(coordinates_file, "r") as file:
        coordinates = json.load(file)
except FileNotFoundError:
    print(f"Error: {coordinates_file} not found.")
    exit()
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON in {coordinates_file}.")
    exit()

# Simulate clicks on the coordinates
print("Starting to simulate clicks...")
for coord in coordinates:
    try:
        x, y = coord
        pyautogui.click(x, y)
        print(f"Clicked at ({x}, {y})")
        time.sleep(0.1)  # 100 ms delay
    except Exception as e:
        print(f"Error clicking at {coord}: {e}")

print("All clicks completed.")
