from typing import Any, List
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import models, schemas
from backend.app.crud import offer as crud


router = APIRouter()


@router.get("/", response_model=List[schemas.Offer])
def read_offers(
        db: Session = Depends(deps.get_db)
        ):
    offers = crud.get_multi(db)
    return offers


@router.get("/{offer_id}", response_model=schemas.Offer)
def read_offer(
        offer_id: int,
        db: Session = Depends(deps.get_db)
        ):
    offer = crud.get(db, offer_id)
    return offer