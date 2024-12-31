# CarRentalService

Based on the FastApi documentation: https://fastapi.tiangolo.com/.

The structure has been decided based on the following article: https://medium.com/@amirm.lavasani/how-to-structure-your-fastapi-projects-0219a6600a8f.

CarRentalService/: Contains the main application files.
main.py: Initializes the FastAPI application.
routers/: Contains router modules.
models/: Contains database model modules.
utils/: Contains utility modules.
services/: Contains service modules.
tests/: Contains test modules.

The project is divided into models, services, routers, and data loading. This ensures that the single responsibility principle is followed. This simplifies the code mantainance, reusability of code and testing.

## Enpoints (example with curl):
- Get car information: curl -X GET "http://127.0.0.1:8010/cars/1"
- Create a booking: curl -X POST "http://127.0.0.1:8010/create_booking/" -H "Content-Type: application/json" -d '{"car_id": 1, "date": "2023-10-02"}'
- Get available cars for a specific date: curl -X GET "http://127.0.0.1:8010/available_cars/?date=2023-10-02"

## Running the Application

### Using Docker

A Dockerfile has been added to perform Dockerization of the application.

**Build the Docker image**:
- docker build -t app_name .
- docker run -d -p 8010:8010 app_name

## Testing

Run the following commands:
- export PYTHONPATH=$(pwd)
- pytest