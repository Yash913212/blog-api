Blog API

A beginner‑friendly REST API that lets you manage **authors** and their **blog posts**. It is built using **FastAPI** and **SQLAlchemy**, and demonstrates a clean **one‑to‑many relationship** where one author can have multiple posts.

This project is ideal for learning how real‑world backend APIs are structured, documented, and connected to a database.

---

Tech Stack (Simple Explanation)

* FastAPI** – Handles HTTP requests and responses quickly and efficiently.
* SQLAlchemy** – Talks to the database using Python objects instead of raw SQL.
* SQLite** – A lightweight database stored as a file (perfect for learning).
* Pydantic** – Validates request and response data automatically.
* Uvicorn** – Runs the FastAPI application.

---

How to Run the Application

Clone the Repository

```bash
git clone <repository-url>
cd blog-api
```

Create & Activate Virtual Environment

Windows

```
bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux

```
bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Dependencies

```
bash
pip install -r requirements.txt
```

Start the Server

```
bash
uvicorn main:app --reload --port 5000
```

API URL: `http://127.0.0.1:5000`

Swagger Docs: `http://127.0.0.1:5000/docs`

---

Database Design (Explained Simply)

This application uses two tables:

Authors Table

Stores information about blog authors.

* `id` – Unique author ID
* `name` – Author name
* `email` – Author email

Posts Table

Stores blog posts written by authors.

* `id` – Unique post ID
* `title` – Post title
* `content` – Post content
* `author_id` – Links the post to an author

Relationship**: One author → Many posts

Cascade Delete**: If an author is deleted, all their posts are deleted automatically.

### ER Diagram

```
Authors (1) ──────── (Many) Posts
```

---

 API Endpoints 
-- Authors API

 Create Author

POST /authors/

Creates a new author.

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

---
Get All Authors

GET /authors/**

Returns a list of all authors.

---

 Get Author by ID

GET /authors/{id}**

Returns a single author. If the ID doesn’t exist, a 404 error is returned.

---
 Update Author

PUT /authors/{id}**

Updates an author’s name or email.

---
 Delete Author

DELETE /authors/{id}

Deletes an author **and all their posts**.

--- Posts API

Create Post

```json
{
  "title": "My First Post",
  "content": "This is the content",
  "author_id": 1
}

---
Get Post by ID


Returns a single post along with author details.

---

Update Post


Updates the post title or content.

---
Delete Post

Deletes a post permanently.


 Nested Resource
 Get Posts by Author

Returns all posts written by a specific author.

 What You Learn From This Project

* REST API design using FastAPI
* One‑to‑Many database relationships
* SQLAlchemy ORM usage
* Data validation with Pydantic
* Clean API documentation
* Real‑world CRUD operations

 Ideal For

* Backend beginners
* FastAPI learners
* Interview practice
* College assignments
* Portfolio projects

