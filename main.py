from fastapi import FastAPI
from app.api.endpoints.registration import registration_router



app = FastAPI()

app.include_router(registration_router)

