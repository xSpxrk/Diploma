from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app import crud, models, schemas
from backend.app.api import deps
from backend.app.core import security

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
def login_access_token(
        *,
        db: Session = Depends(deps.get_db),
        login: schemas.Login
) -> Any:
    user = crud.customer.authenticate(db, email=login.username, password=login.password)
    type = "customer"
    if not user:
        user = crud.provider.authenticate(db, email=login.username, password=login.password)
        type = "provider"
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": security.create_access_token(
            user.customer_id if type == "customer" else user.provider_id,
            type,
            expires_delta=None
        ),
        "token_type": "bearer",
        "type": type
    }
