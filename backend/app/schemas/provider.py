from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .offer import Offer


class ProviderBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int


class Provider(ProviderBase):
    provider_id: int
    offers: List[Offer] = []

    class Config:
        orm_mode = True


class ProviderCreate(ProviderBase):
    password: str


class ProviderUpdate(ProviderBase):
    password: Optional[str] = None
