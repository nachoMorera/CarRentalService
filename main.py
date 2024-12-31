from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

with open('car.json') as f:
    cars = json.load(f)
class Car(BaseModel):
    id: int
    brand: str
    model: str
    available_date: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/cars/{car_id}")
def read_car(car_id: int):
    car = next((car for car in cars if car["id"] == car_id), None)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@app.get("/available_cars/", response_model=List[Car])
def get_available_cars(date: str):
    available_cars = [car for car in cars if car["available_date"] == date]
    if not available_cars:
        raise HTTPException(status_code=404, detail="No cars available on this date")
    return available_cars