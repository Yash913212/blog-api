# Blog API

A RESTful API for a simple blog platform that manages authors and their corresponding posts, focusing on one-to-many relationships.

## Setup

1. Clone the repository.
2. Create a virtual environment (optional but recommended): `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `uvicorn main:app --reload`

The API will be available at `http://127.0.0.1:8000`

You can also access the interactive API documentation at `http://127.0.0.1:8000/docs`

## Database Schema

The database uses SQLite with the following tables:

- **authors**
  - id: INTEGER PRIMARY KEY AUTOINCREMENT
  - name: VARCHAR NOT NULL
  - email: VARCHAR UNIQUE NOT NULL

- **posts**
  - id: INTEGER PRIMARY KEY AUTOINCREMENT
  - title: VARCHAR NOT NULL
  - content: TEXT NOT NULL
  - author_id: INTEGER NOT NULL, FOREIGN KEY REFERENCES authors(id) ON DELETE CASCADE

Entity-Relationship Diagram:

```
authors (1) -----> (*) posts
  - id (PK)
  - name
  - email (UQ)

posts
  - id (PK)
  - title
  - content
  - author_id (FK)
```

The relationship is one-to-many: one author can have many posts. Deleting an author cascades to delete all their posts.

## API Endpoints

### Authors

- **POST /authors/**: Create a new author.
  - Body: `{"name": "string", "email": "string"}`
  - Response: Author object
  - Status: 200 OK, 400 Bad Request (email already exists)

- **GET /authors/**: Get all authors.
  - Query params: skip (default 0), limit (default 100)
  - Response: List of Author objects

- **GET /authors/{id}**: Get author by ID.
  - Response: Author object
  - Status: 200 OK, 404 Not Found

- **PUT /authors/{id}**: Update author.
  - Body: `{"name": "string", "email": "string"}`
  - Response: Author object
  - Status: 200 OK, 404 Not Found, 400 Bad Request (email already exists)

- **DELETE /authors/{id}**: Delete author (cascades to posts).
  - Status: 200 OK with message, 404 Not Found

### Posts

- **POST /posts/**: Create a new post.
  - Body: `{"title": "string", "content": "string", "author_id": int}`
  - Response: Post object with author
  - Status: 200 OK, 400 Bad Request (author not found)

- **GET /posts/**: Get all posts, optionally filter by author_id.
  - Query params: skip (default 0), limit (default 100), author_id (optional)
  - Response: List of Post objects with author details

- **GET /posts/{id}**: Get post by ID with author details.
  - Response: Post object with author
  - Status: 200 OK, 404 Not Found

- **PUT /posts/{id}**: Update post.
  - Body: `{"title": "string", "content": "string"}` (partial update allowed)
  - Response: Post object
  - Status: 200 OK, 404 Not Found

- **DELETE /posts/{id}**: Delete post.
  - Status: 200 OK with message, 404 Not Found

- **GET /authors/{id}/posts**: Get all posts by author.
  - Response: List of Post objects
  - Status: 200 OK, 404 Not Found (author not found)

## Example Requests

Create author:
```
POST /authors/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}

Response (201):
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

Create post:
```
POST /posts/
Content-Type: application/json

{
  "title": "My First Post",
  "content": "This is the content.",
  "author_id": 1
}

Response (201):
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content.",
  "author_id": 1,
  "author": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

Get posts:
```
GET /posts/

Response (200):
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "This is the content.",
    "author_id": 1,
    "author": {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
]
```

Get post with author:
```
GET /posts/1

Response (200):
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content.",
  "author_id": 1,
  "author": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
}
```

Error example (create post with invalid author):
```
POST /posts/
Content-Type: application/json

{
  "title": "Post",
  "content": "Content",
  "author_id": 999
}

Response (400):
{
  "detail": "Author not found"
}
```

## Testing

Import the `postman_collection.json` file into Postman to test all endpoints. Set the `base_url` variable to your API URL (default: http://127.0.0.1:8000).

## Technologies Used

- FastAPI: Web framework
- SQLAlchemy: ORM for database interactions
- SQLite: Database
- Pydantic: Data validation
- Uvicorn: ASGI server