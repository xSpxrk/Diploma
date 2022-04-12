from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.app.models.customer import Customer

from backend.app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    def create(
            self,
            db: Session,
            obj_in: CustomerCreate
    ) -> Customer:
        pass


customer = CRUDCustomer(Customer)



