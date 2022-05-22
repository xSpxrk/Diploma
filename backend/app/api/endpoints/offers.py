from typing import Any, List
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import models, schemas
from backend.app import crud
from backend.app.models import Provider

router = APIRouter()


@router.get("/", response_model=List[schemas.Offer])
def read_offers(
        db: Session = Depends(deps.get_db)
):
    offers = crud.offer.get_multi(db)
    return offers


@router.get("/{offer_id}", response_model=schemas.Offer)
def read_offer(
        offer_id: int,
        db: Session = Depends(deps.get_db)
):
    offer = crud.offer.get(db, offer_id)
    return offer


@router.post("/", response_model=schemas.Offer)
def create_offer(
        *,
        db: Session = Depends(deps.get_db),
        offer_in: schemas.OfferCreate,
        user: Provider = Depends(deps.get_current_user)
):
    offer_in.provider_id = user.provider_id
    offer = crud.offer.create(db, offer_in)
    return offer


@router.put("/update/{offer_id}", response_model=schemas.Offer)
def update_offer(
        *,
        db: Session = Depends(deps.get_db),
        offer_in: schemas.OfferUpdate,
        offer_id: int,
):
    offer = crud.offer.get(db, offer_id)
    if not offer:
        raise HTTPException(
            status_code=404,
            detail="The offer with this id doesnt exist"
        )
    offer = crud.offer.update(db, db_obj=offer, obj_in=offer_in)
    return offer
