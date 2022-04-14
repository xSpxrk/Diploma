from pydantic import BaseModel
from .offer import Offer as offer
from typing import List


class OrderBase(BaseModel):
    name: str
    description: str
    materials: str
    quantity: int


class Order(OrderBase):
    order_id: int
    offers: List[offer]
    customer_id: int

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass
