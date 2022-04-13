from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.app.models.customer import Customer
from backend.app.core.security import hash_password

from backend.app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):

    def get(self, db: Session, id: id) -> Optional[Customer]:
        return db.query(self.model).filter(self.model.customer_id == id).first()

    def create(
            self,
            db: Session,
            obj_in: CustomerCreate
    ) -> Customer:
        new_customer = Customer(
            name=obj_in.name,
            email=obj_in.email,
            phone_number=obj_in.phone_number,
            hashed_password=hash_password(obj_in.password)
        )
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
        return new_customer


customer = CRUDCustomer(Customer)



