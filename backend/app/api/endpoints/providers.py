from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app.models import Provider as ModelProvider
from backend.app.schemas import Provider as SchemaProvider
from backend.app import crud

router = APIRouter()


@router.get("/", response_model=List[SchemaProvider])
def read_providers(
        db: Session = Depends(deps.get_db)
        ):
    providers = crud.provider.get_multi(db)
    return providers


@router.get("/{provider_id}", response_model=SchemaProvider)
def read_provider(
        provider_id: int,
        db: Session = Depends(deps.get_db)
        ):
    provider = crud.provider.get(db, provider_id)
    return provider


