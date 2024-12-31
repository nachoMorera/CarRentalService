from fastapi import FastAPI
import logging
from routers import car_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(car_router.router)