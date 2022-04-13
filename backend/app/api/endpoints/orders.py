from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app.schemas import Order
from backend.app import crud

router = APIRouter()


@router.get("/", response_model=List[Order])
def read_providers(
        db: Session = Depends(deps.get_db)
        ):
    orders = crud.order.get_multi(db)
    return orders


@router.get("/{order_id}", response_model=Order)
def read_provider(
        order_id: int,
        db: Session = Depends(deps.get_db)
        ):
    order = crud.order.get(db, order_id)
    return order
