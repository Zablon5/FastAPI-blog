from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

def delete(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with id {id} is not available")

    blog.delete(synchronize_session=False)
    db.commit()
    return'done'

def get_blog(db:Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog with id {id} is not available.")
    return blog
def update(db:Session, request:schemas.Blog, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the blog with id {id} is not available")
    
    blog.update(request.model_dump())
    db.commit()
    return 'done'