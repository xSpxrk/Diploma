from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.app.models import Provider
from backend.app.schemas.provider import ProviderCreate, ProviderUpdate


class CRUDProvider(CRUDBase[Provider, ProviderCreate, ProviderUpdate]):

    def get(self, db: Session, id: int) -> Provider:
        return db.query(self.model).filter(self.model.provider_id == id).first()

    def create(
            self,
            db: Session,
            obj_in: ProviderCreate
    ) -> Provider:
        pass


provider = CRUDProvider(Provider)
