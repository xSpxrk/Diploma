from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import schemas
from backend.app import crud

router = APIRouter()


@router.get("/", response_model=List[schemas.Order])
def read_orders(
        db: Session = Depends(deps.get_db)
):
    orders = crud.order.get_multi(db)
    return orders


@router.get("/{order_id}", response_model=schemas.Order)
def read_order(
        order_id: int,
        db: Session = Depends(deps.get_db)
):
    order = crud.order.get(db, order_id)
    return order


@router.post("/", response_model=schemas.Order)
def create_order(
        *,
        db: Session = Depends(deps.get_db),
        order_in: schemas.OrderCreate,
        order_id: int
):
    order = crud.order.create(db, order_in, order_id)
    return order


@router.put("/update/{order_id}", response_model=schemas.Order)
def update_order(
        *,
        db: Session = Depends(deps.get_db),
        order_in: schemas.OrderUpdate,
        order_id: int
):
    order = crud.order.get(db, order_id)
    if not order:
        raise HTTPException(
            status_code=404,
            detail="The offer with this id doesnt exist"
        )
    order = crud.order.update(db, db_obj=order, obj_in=order_in)
    return order
