from fastapi import FastAPI
from routers import get_blogs, post_blogs
from db import models
from db.database import engine

app = FastAPI()

app.include_router(get_blogs.router)
app.include_router(post_blogs.router)


@app.get('/')
def index():
    return {"message":"Hello World!"}


models.Base.metadata.create_all(engine)