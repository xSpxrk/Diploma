from .base import CRUDBase
from backend.app.models import Order
from sqlalchemy.orm import Session
from typing import Optional
from backend.app.schemas.order import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):

    def get(self, db: Session, order_id: int) -> Optional[Order]:
        return db.query(self.model).filter(self.model.order_id == order_id).first()


order = CRUDOrder(Order)
