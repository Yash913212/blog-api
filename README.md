# Blog API

A simple RESTful API for managing authors and their posts using a one-to-many relationship.

## Setup

1. Clone the repository
2. (Optional) Create a virtual environment: `python -m venv .venv`
3. Activate it (Windows): `.venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn main:app --reload --port 5000`

API URL: `http://127.0.0.1:5000`  
Swagger Docs: `http://127.0.0.1:5000/docs`

## API Endpoints

### Authors
- `POST /authors/` – Create an author
- `GET /authors/` – Get all authors
- `GET /authors/{id}` – Get author by ID
- `PUT /authors/{id}` – Update author
- `DELETE /authors/{id}` – Delete author

### Posts
- `POST /posts/` – Create a post
- `GET /posts/` – Get all posts (filter by `author_id`)
- `GET /posts/{id}` – Get post by ID
- `PUT /posts/{id}` – Update post
- `DELETE /posts/{id}` – Delete post
- `GET /authors/{id}/posts` – Get all posts by an author

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Resources

- **Designing a RESTful API with Foreign Keys**  
  A guide on how to handle nested resources and relationships in REST API design.

- **What is an ORM and How to Use It**  
  An introduction to Object-Relational Mapping (ORM), a key tool for working with databases in modern applications.

- **The N+1 Query Problem**  
  An article explaining the common N+1 query performance issue and strategies to solve it, particularly with ORMs.

- **PostgreSQL Foreign Key Constraints**  
  Official PostgreSQL documentation on how to use foreign key constraints.