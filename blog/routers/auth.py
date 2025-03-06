from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, JWTtoken
from sqlalchemy.orm import Session
from blog import schemas
from ..hashing import Hash


router = APIRouter(prefix='/login',tags=['Auth'], )

@router.post('/')
def login_user(request:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credential')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return access_token
