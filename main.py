from fastapi import FastAPI
from routers import get_blogs, post_blogs


app = FastAPI()

app.include_router(get_blogs.router)
app.include_router(post_blogs.router)


@app.get('/')
def index():
    return {"message":"Hello World!"}
