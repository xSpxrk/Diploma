from pydantic import BaseModel, EmailStr
from typing import List


class ProviderBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int


class Provider(ProviderBase):
    provider_id: int

    class Config:
        orm_mode = True


class ProviderCreate(ProviderBase):
    pass


class ProviderUpdate(ProviderBase):
    pass
