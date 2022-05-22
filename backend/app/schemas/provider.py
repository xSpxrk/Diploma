from pydantic import BaseModel, EmailStr
from typing import List, Optional


class ProviderBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int


class Provider(ProviderBase):
    provider_id: int

    class Config:
        orm_mode = True


class ProviderCreate(ProviderBase):
    password: str


class ProviderUpdate(ProviderBase):
    password: Optional[str] = None
