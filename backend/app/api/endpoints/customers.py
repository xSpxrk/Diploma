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


@router.get('/{customer_id}', response_model=schemas.Customer)
def read_customer(
        customer_id: int,
        db: Session = Depends(deps.get_db)
):
    customer = crud.customer.get(db, customer_id)
    return customer


@router.post('/', response_model=schemas.Customer)
def create_customer(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.CustomerCreate
) -> Any:
    user = crud.customer.create(db, user_in)
    return user


@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer(
        *,
        db: Session = Depends(deps.get_db),
        customer_id: int,
        customer_in: schemas.CustomerUpdate,
) -> Any:
    customer = crud.customer.get(db, customer_id)
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="The customer with this id doesnt exist"
        )
    customer = crud.customer.update(db, db_obj=customer, obj_in=customer_in)
    return customer

