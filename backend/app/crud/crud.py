import logging

from sqlalchemy.orm import Session
from backend.app import models


def get_customers(db: Session):
    return db.query(models.Customer).all()


def get_orders(db: Session, id: int):
    return db.query(models.Order).filter(models.Order.customer_id == id).all()
