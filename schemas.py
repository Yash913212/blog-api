from pydantic import BaseModel, field_validator
from typing import Optional


class AuthorBase(BaseModel):
    name: str
    email: str
    
    @field_validator('name', 'email')
    @classmethod
    def validate_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Field cannot be empty')
        return v.strip()


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
    
    @field_validator('title', 'content')
    @classmethod
    def validate_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Field cannot be empty')
        return v.strip()


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
