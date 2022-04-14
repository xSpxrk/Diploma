from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app.schemas import Order, OrderCreate
from backend.app import crud

router = APIRouter()


@router.get("/", response_model=List[Order])
def read_orders(
        db: Session = Depends(deps.get_db)
        ):
    orders = crud.order.get_multi(db)
    return orders


@router.get("/{order_id}", response_model=Order)
def read_order(
        order_id: int,
        db: Session = Depends(deps.get_db)
        ):
    order = crud.order.get(db, order_id)
    return order


@router.post("/create/{customer_id}", response_model=Order)
def create_order(
        *,
        db: Session = Depends(deps.get_db),
        order_in: OrderCreate,
        customer_id: int
):
    order = crud.order.create(db, order_in, customer_id)
    return order
