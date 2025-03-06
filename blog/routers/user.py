from fastapi import APIRouter, Depends, HTTPException, status

from blog.hashing import Hash
from .. import models,database,schemas
from ..repository import user_repo
from typing import List
from sqlalchemy.orm import Session

get_db = database.get_db
router = APIRouter(tags=['users'], prefix='/user')

@router.post('/', response_model=schemas.ResponseUser,  )
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user_repo.create_user(request,db)


@router.get('/{id}', response_model=schemas.ResponseUser,  )
def get_user(id:int, db:Session=Depends(get_db)):
    return user_repo.get_user(db, id)