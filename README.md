# Blog API

A RESTful API for managing authors and posts with one-to-many relationships.

## Setup

1. Clone the repo
2. `python -m venv .venv` (optional)
3. `.venv\Scripts\activate` (Windows)
4. `pip install -r requirements.txt`
5. `uvicorn main:app --reload`

API at `http://127.0.0.1:5000`, docs at `/docs`

## Endpoints

### Authors
- `POST /authors/` - Create author
- `GET /authors/` - List authors
- `GET /authors/{id}` - Get author
- `PUT /authors/{id}` - Update author
- `DELETE /authors/{id}` - Delete author

### Posts
- `POST /posts/` - Create post
- `GET /posts/` - List posts (filter by author_id)
- `GET /posts/{id}` - Get post
- `PUT /posts/{id}` - Update post
- `DELETE /posts/{id}` - Delete post
- `GET /authors/{id}/posts` - Get author's posts

## Technologies
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn