from typing import Any, List, Union, Optional
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session
from backend.app.api import deps
from backend.app import models, schemas
from backend.app import crud

router = APIRouter()


@router.get('/{user_id}', response_model=Union[schemas.Provider, schemas.Customer])
def read_me(
        db: Session = Depends(deps.get_db),
        current_user: Union[models.Customer, models.Provider] = Depends(deps.get_current_user)
):
    if isinstance(current_user, models.Customer):
        user = crud.customer.get(db, current_user.customer_id)
    else:
        user = crud.provider.get(db, current_user.provider_id)
    return user


@router.put("/{user_id}", response_model=Union[schemas.Provider, schemas.Customer])
def update_me(
        *,
        db: Session = Depends(deps.get_db),
        user_in: Union[schemas.ProviderUpdate, schemas.CustomerUpdate],
        current_user: Union[models.Customer, models.Provider] = Depends(deps.get_current_user)
) -> Any:
    if isinstance(current_user, models.Customer):
        obj = crud.customer.get(db, current_user.customer_id)
        user = crud.customer.update(db, db_obj=obj, obj_in=user_in)
    else:
        obj = crud.provider.get(db, current_user.provider_id)
        user = crud.provider.update(db, db_obj=obj, obj_in=user_in)
    return user
