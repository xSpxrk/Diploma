from fastapi import FastAPI, Depends, APIRouter

from .endpoints import customers


app = FastAPI()

app.include_router(customers.router, prefix="/customers", tags=["customers"])
