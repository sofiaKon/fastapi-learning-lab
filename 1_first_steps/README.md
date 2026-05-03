# FastAPI Basics Practice
## Project Overview

This project demonstrates the fundamental concepts of building a simple API using FastAPI.
It covers basic routing, HTTP methods, and how FastAPI handles requests and responses.

The goal was to understand how an API is structured and how different types of endpoints work.

---

## HTTP Methods

Implemented core REST operations:

- GET → retrieve data
- POST → create new data
- PUT → update existing data
- DELETE → remove data

---

## Async vs Sync Functions

- Used async def for asynchronous endpoints
- Used def for synchronous example
- Learned when each approach is appropriate

---
##bAutomatic API Documentation

FastAPI provides built-in documentation:

- /docs → Swagger UI
- /redoc → ReDoc
- /openapi.json → OpenAPI schema

---
## How to Run the Project

```bash
uvicorn main:app --reload
```

```bash
http://127.0.0.1:8000/docs
```

---

## Key Takeaways
- FastAPI makes it easy to build APIs quickly
- Type hints are used for validation and data conversion
- Minimal code is required to create fully functional endpoints
- Built-in documentation simplifies testing and debugging