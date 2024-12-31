from typing import List
from fastapi import APIRouter, HTTPException
import json
from models.models import Car, Booking
from services.booking_service import create_booking

router = APIRouter()

with open('data/cars.json') as f:
    cars = json.load(f)
with open('data/bookings.json', "r") as file:
    bookings = json.load(file)

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/cars/{car_id}")
def read_car(car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.get("/available_cars/", response_model=List[Car])
def get_available_cars(date: str):
    available_cars = [car for car in cars if car["available_date"] == date]
    if not available_cars:
        raise HTTPException(status_code=404, detail="No cars available on this date")
    return available_cars

@router.post("/create_booking/")
def create_booking_endpoint(booking: Booking):
    new_booking = create_booking(booking)
    return {"message": "Booking created successfully", "booking": new_booking}