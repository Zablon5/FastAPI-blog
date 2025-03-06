from fastapi import APIRouter, Depends, HTTPException, status
from .. import models,database,schemas, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog_repo
router = APIRouter(tags=['blogs'], prefix='/blog')


@router.get('/', response_model=List[schemas.ResponseBlog] )
def blogs(db:Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.get_all(db)
    

@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request:schemas.Blog, db:Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.create(request, db)


@router.get('/{id}',  status_code=status.HTTP_200_OK, response_model=schemas.ResponseBlog, )
def blog(id, db:Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.get_blog(db, id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, )
def delete_blog(id, db:Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, )
def update_blog(id,request:schemas.Blog,db:Session=Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    
    return blog_repo.update(db,request,id)