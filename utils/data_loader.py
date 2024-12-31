import json
from pathlib import Path

def load_data(file_path: Path):
    with open(file_path, "r") as file:
        return json.load(file)

def save_data(file_path: Path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

cars_path = Path("data/cars.json")
bookings_path = Path("data/bookings.json")

cars = load_data(cars_path)
bookings = load_data(bookings_path)