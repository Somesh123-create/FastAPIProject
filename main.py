from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {"message":"Hello World!"}


#parameter
# @app.get('/blog/all')
# def all_blog():
#     return {"message":"all blog provided."}


#query parameter
@app.get('/blog/all', tags=['blog'])
def all_blog(page=1, page_size:Optional[int]=None):
    return {"message":f"all {page_size} blog on page: {page}"}



class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get('/blog/type/{type}', tags=['blog'])
def blog_types(type: BlogType):
    return {"message":f"Blog Type: {type}"}


@app.get('/blog/{blog_id}/comment/{comment_id}', tags=['blog', 'comment'])
def comments(blog_id:int, comment_id:int, valid:bool = True, username: Optional[str] = None):
    return {"message":f"blog_id : {blog_id}, comment_id: {comment_id}, valid: {valid}, username:{username}"}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response:Response):
    if id > 7:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
        return {"message":f"blog with id: {id}"}
