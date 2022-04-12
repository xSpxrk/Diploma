from pydantic import BaseModel


class OrderBase(BaseModel):
    name: str
    description: str
    materials: str
    quantity: int


class Order(OrderBase):
    order_id: int

    class Config:
        orm_mode = True

