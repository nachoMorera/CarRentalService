
from pathlib import Path
from datetime import datetime
from fastapi import HTTPException
from models.models import Booking
from utils.data_loader import load_data, save_data

def create_booking(booking: Booking):
    cars_path = Path("data/cars.json")
    bookings_path = Path("data/bookings.json")

    cars = load_data(cars_path)
    bookings = load_data(bookings_path)

    car = next((car for car in cars if car["id"] == booking.car_id), None)
    if not car:
        raise HTTPException(status_code=400, detail="Car not found")

    available_date = datetime.strptime(car["available_date"], "%Y-%m-%d")
    booking_date = datetime.strptime(booking.date, "%Y-%m-%d")

    if booking_date <= available_date:
        raise HTTPException(status_code=400, detail="The booking date must be after the available date.")

    new_booking = {"car_id": booking.car_id, "date": booking.date}
    bookings.append(new_booking)
    save_data(bookings_path, bookings)

    return new_booking