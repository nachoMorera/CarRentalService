from typing import List
from fastapi import FastAPI, HTTPException
from pathlib import Path
from datetime import datetime
import json
import logging
from models.models import Car, Booking

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

with open('cars.json') as f:
    cars = json.load(f)
with open('bookings.json', "r") as file:
    bookings = json.load(file)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"Hello": "World"}

@app.get("/cars/{car_id}")
def read_car(car_id: int):
    logger.info(f"Fetching car with ID: {car_id}")
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        logger.error(f"Car with ID {car_id} not found")
        raise HTTPException(status_code=404, detail="Car not found")
    logger.info(f"Car found: {car}")
    return car

@app.get("/available_cars/", response_model=List[Car])
def get_available_cars(date: str):
    logger.info(f"Fetching available cars for date: {date}")
    available_cars = [car for car in cars if car["available_date"] == date]
    if not available_cars:
        logger.error(f"No cars available on date: {date}")
        raise HTTPException(status_code=404, detail="No cars available on this date")
    logger.info(f"Available cars: {available_cars}")
    return available_cars

@app.post("/create_booking/")
def create_booking(booking: Booking):
    logger.info(f"Creating booking for car ID: {booking.car_id} on date: {booking.date}")

    car = next((car for car in cars if car["id"] == booking.car_id), None)
    if not car:
        logger.error(f"Car with ID {booking.car_id} not found")
        raise HTTPException(status_code=400, detail="Car not found")

    available_date = datetime.strptime(car["available_date"], "%Y-%m-%d")
    booking_date = datetime.strptime(booking.date, "%Y-%m-%d")

    if booking_date <= available_date:
        logger.error(f"The booking date {booking.date} must be after the available date {car['available_date']}")
        raise HTTPException(status_code=400, detail="The booking date must be after the available date.")

    new_booking = {"car_id": booking.car_id, "date": booking.date}
    bookings.append(new_booking)
    with open('bookings.json', "w") as file:
        json.dump(bookings, file, indent=4)

    logger.info(f"Booking created successfully: {new_booking}")
    return {"message": "Booking created successfully", "booking": new_booking}