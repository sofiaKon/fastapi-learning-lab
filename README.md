# FastAPI Learning Lab

## Overview
This repository contains my hands-on practice while learning FastAPI.  
It covers core concepts required to build modern APIs, including routing, validation, request handling, and structured query models.

The project is organized into small modules, each focusing on a specific concept.

---

## Project Structure
```bash
fastapi-learning-lab/
│
├── 1_first_steps/ # basic setup and simple routes
├── path_param/ # path parameters and dynamic routing
├── query_param/ # query parameters and filtering
│ ├── numeric_validation/
│ ├── string_validation/
│ └── models/
├── request_body/ # working with JSON and Pydantic
└── README.md 
```

---

## Topics Covered

### 1. First Steps
- FastAPI app creation
- Basic endpoints
- HTTP methods (GET, POST, PUT, DELETE)

---

### 2. Path Parameters
- Dynamic routing using URL values
- Type validation
- Enum for predefined values

---

### 3. Query Parameters
- Passing data through URL
- Optional and required parameters
- Boolean parameters

---

### 4. Validation
- Numeric validation with `Path()`
- String validation with `Query()`
- Regex and length constraints

---

### 5. Request Body
- Using Pydantic models
- JSON input/output
- Combining body with path/query params

---

### 6. Query Parameter Models
- Grouping parameters into models
- Using `Field()` for validation
- Restricting extra inputs

---

## How to Run

```bash
uvicorn main:app --reload
```
Then open:

```bash
http://127.0.0.1:8000/docs
```
