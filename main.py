from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import crud
from schemas import *
from typing import List, Optional

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/authors/", response_model=Author, status_code=201)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.get_author_by_email(db, author.email)
    if db_author:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_author(db, author)


@app.get("/authors/", response_model=List[Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors


@app.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@app.put("/authors/{author_id}", response_model=Author)
def update_author_endpoint(
    author_id: int, author: AuthorCreate, db: Session = Depends(get_db)
):
    db_author = crud.update_author(db, author_id, author)
    if db_author is None:
        raise HTTPException(
            status_code=404, detail="Author not found or email already registered"
        )
    return db_author


@app.delete("/authors/{author_id}")
def delete_author_endpoint(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted"}


@app.post("/posts/", response_model=Post, status_code=201)
def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    if db_post is None:
        raise HTTPException(status_code=400, detail="Author not found")
    return db_post


@app.get("/posts/", response_model=List[Post])
def read_posts(
    skip: int = 0,
    limit: int = 100,
    author_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    posts = crud.get_posts(db, skip=skip, limit=limit, author_id=author_id)
    return posts


@app.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.put("/posts/{post_id}", response_model=Post)
def update_post_endpoint(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@app.delete("/posts/{post_id}")
def delete_post_endpoint(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}


@app.get("/authors/{author_id}/posts", response_model=List[Post])
def read_posts_by_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    posts = crud.get_posts_by_author(db, author_id)
    return posts
