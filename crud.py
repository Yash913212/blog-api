from sqlalchemy.orm import Session, joinedload
from models import Author, Post
from schemas import AuthorCreate, PostCreate, PostUpdate
from typing import Optional


def get_author_by_email(db: Session, email: str):
    return db.query(Author).filter(Author.email == email).first()


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: int, author: AuthorCreate):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        if author.email != db_author.email:
            existing = get_author_by_email(db, author.email)
            if existing:
                return None
        db_author.name = author.name
        db_author.email = author.email
        db.commit()
        db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if db_author:
        db.delete(db_author)
        db.commit()
    return db_author


def get_post(db: Session, post_id: int):
    return (
        db.query(Post)
        .options(joinedload(Post.author))
        .filter(Post.id == post_id)
        .first()
    )


def get_posts(
    db: Session, skip: int = 0, limit: int = 100, author_id: Optional[int] = None
):
    query = db.query(Post).options(joinedload(Post.author))
    if author_id:
        query = query.filter(Post.author_id == author_id)
    return query.offset(skip).limit(limit).all()


def create_post(db: Session, post: PostCreate):
    # Check if author exists
    author = db.query(Author).filter(Author.id == post.author_id).first()
    if not author:
        return None
    db_post = Post(title=post.title, content=post.content, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post_id: int, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        if post.title is not None:
            db_post.title = post.title
        if post.content is not None:
            db_post.content = post.content
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post


def get_posts_by_author(db: Session, author_id: int):
    return db.query(Post).filter(Post.author_id == author_id).all()
