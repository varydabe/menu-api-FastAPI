from fastapi import FastAPI
from mongoengine import connect
from app.cores.config import Config
from starlette.testclient import TestClient

from app.routers import menus

app = FastAPI()

mongodb = connect('mongodb', host=Config.MONGO_URL)
client = TestClient(app)

app.include_router(menus.router, prefix="/menus", tags=["Menu Docs"], )