from fastapi import FastAPI
from . import models
from .database import engine


from .routers import blog, user, auth
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app on Vercel!"}
models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)



