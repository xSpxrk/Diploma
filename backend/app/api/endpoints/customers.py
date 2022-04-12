from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import models, schemas
from backend.app import crud


router = APIRouter()


@router.get("/", response_model=List[schemas.Customer])
def read_customers(
        db: Session = Depends(deps.get_db)
        ):
    customers = crud.customer.get_multi(db)
    return customers
