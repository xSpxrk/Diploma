from typing import List, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import schemas
from backend.app import crud

router = APIRouter()


@router.get("/", response_model=List[schemas.Provider])
def read_providers(
        db: Session = Depends(deps.get_db)
):
    providers = crud.provider.get_multi(db)
    return providers


@router.get("/{provider_id}", response_model=schemas.Provider)
def read_provider(
        provider_id: int,
        db: Session = Depends(deps.get_db)
):
    provider = crud.provider.get(db, provider_id)
    return provider


@router.post('/', response_model=schemas.Provider)
def create_customer(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.ProviderCreate
) -> Any:
    user = crud.provider.create(db, user_in)
    return user
