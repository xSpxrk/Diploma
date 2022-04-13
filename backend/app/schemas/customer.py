from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .order import Order


class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int


class CustomerCreate(CustomerBase):
    email: EmailStr
    password: str


class Customer(CustomerBase):
    orders: List[Order] = []

    class Config:
        orm_mode = True


class CustomerUpdate(CustomerBase):
    password: str



