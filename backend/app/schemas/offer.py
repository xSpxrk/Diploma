from pydantic import BaseModel
from decimal import Decimal
from typing import List, Optional
from .provider import Provider


class OfferBase(BaseModel):
    quantity: int
    price: Decimal
    order_id: int
    provider_id: int


class Offer(OfferBase):
    offer_id: int
    provider: Optional[Provider]

    class Config:
        orm_mode = True


class OfferCreate(OfferBase):
    pass


class OfferUpdate(OfferBase):
    pass
