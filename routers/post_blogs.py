from fastapi import APIRouter, Query, Path, Body
from typing import Optional, List, Dict
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["bog"]
)


class Image(BaseModel):
    url : str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None


#path params and query params
@router.post("/new/{id}")
def create_blog(blog:BlogModel, id: int, version:int =1):
    return {
        "id":id,
        "data":blog,
        "version":version
        }


#parameters
@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog:BlogModel,
                   id: int,
                   blog_id: int = Query(None,title="Id of the comment",description="Some description for blog_id",alias="blogId",deprecated=True),
                   content: str = Body("Hello How are you."),
                   note: str = Body(..., min_length=10, max_length=25, regex="^[a-z\s]*$"),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
                   comment_id: int = Path(gt=5, le=10)
                   ):
    return {
        "blog":blog,
        "id":id,
        "blog_id":blog_id,
        "comment_id":comment_id,
        "content":content,
        "note":note,
        "version":v
    }