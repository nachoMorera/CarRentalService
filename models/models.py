from pydantic import BaseModel

class Car(BaseModel):
    id: int
    brand: str
    model: str
    available_date: str

class Booking(BaseModel):
    car_id: int
    date: str