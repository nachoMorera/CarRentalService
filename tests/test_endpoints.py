from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_car():
    response = client.get("/cars/1")
    assert response.status_code == 200

def test_get_available_cars():
    response = client.get("/available_cars/?date=2025-01-02")
    assert response.status_code == 200

def test_create_booking():
    response = client.post(
        "/create_booking/",
        json={"car_id": 1, "date": "2025-03-02"}
    )
    assert response.status_code == 200
