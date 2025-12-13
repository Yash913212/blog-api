from pydantic import BaseModel
from typing import Optional


class AuthorBase(BaseModel):
    name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str
    author_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author: Optional[Author] = None

    class Config:
        from_attributes = True


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
