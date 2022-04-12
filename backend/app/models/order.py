from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base_class import Base


class Order(Base):
    order_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    materials = Column(String)
    quantity = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    owner = relationship("Customer", back_populates="orders")
