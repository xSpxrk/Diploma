from .base import CRUDBase
from backend.app.models import Offer
from sqlalchemy.orm import Session
from backend.app.schemas.offer import OfferCreate, OfferUpdate


class CRUDOffer(CRUDBase[Offer, OfferCreate, OfferUpdate]):

    def get(self, db: Session, offer_id: int) -> Offer:
        return db.query(self.model).filter(self.model.offer_id == offer_id).first()


offer = CRUDOffer(Offer)
