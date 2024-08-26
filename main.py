from fastapi import FastAPI
from routers import get_blogs, post_blogs, user, article
from db import models
from db.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI()

app.include_router(user.router)
app.include_router(article.router)
app.include_router(get_blogs.router)
app.include_router(post_blogs.router)


@app.get('/')
def index():
    return {"message":"Hello World!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content = {"detail": exc.name}
    )

models.Base.metadata.create_all(engine)
