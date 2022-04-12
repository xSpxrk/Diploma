from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .order import Order


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: int


class CustomerCreate(CustomerBase):
    email: EmailStr


class Customer(CustomerBase):
    orders: List[Order] = []

    class Config:
        orm_mode = True


class CustomerUpdate():
    pass



