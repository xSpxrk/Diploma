from fastapi import FastAPI, Depends, APIRouter

from .endpoints import customers, offers, providers, orders


app = FastAPI()

app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(offers.router, prefix="/offers", tags=["offers"])
app.include_router(providers.router, prefix="/providers", tags=["providers"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
