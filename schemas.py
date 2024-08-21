from pydantic import BaseModel

#article inside user display
class Article(BaseModel):
    title : str
    content : str
    published : bool
    class Config():
        orm_model: True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    itmes: list[Article] = []
    class Config():
        orm_model: True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


#user inside article display
class User(BaseModel):
    id: int
    username: str
    class Config():
        orm_model: True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        orm_model: True
