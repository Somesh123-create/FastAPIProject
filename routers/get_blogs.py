from enum import Enum
from typing import Optional
from fastapi import APIRouter, status, Response

router = APIRouter(
    prefix="/bog",
    tags=["blog"]
)

#query parameter
@router.get('/all', summary="Retrieve all blogs", description="This api call simulates fetching all blogs", response_description="The list of available blogs")
def all_blog(page=1, page_size:Optional[int]=None):
    return {"message":f"all {page_size} blog on page: {page}"}



class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get('/type/{type}')
def blog_types(type: BlogType):
    return {"message":f"Blog Type: {type}"}


@router.get('/{blog_id}/comment/{comment_id}', tags=['comment'])
def comments(blog_id:int, comment_id:int, valid:bool = True, username: Optional[str] = None):
    """
    simulates retriving a comment of a blog
    - **blog_id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {"message":f"blog_id : {blog_id}, comment_id: {comment_id}, valid: {valid}, username:{username}"}


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response:Response):
    if id > 7:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response.status_code = status.HTTP_200_OK
        return {"message":f"blog with id: {id}"}
