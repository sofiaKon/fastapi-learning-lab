# FastAPI Query Parameter Models Practice

## Overview
This project is based on the official FastAPI tutorial about query parameter models.  
The goal was to learn how to group multiple query parameters into a single structured model using Pydantic.

---

## What I Learned

### 1. Grouping Query Parameters
When multiple query parameters are related, they can be combined into one Pydantic model.

This helps:
- keep code clean  
- reuse parameter structures  
- centralize validation  

FastAPI automatically extracts query values and fills the model. :contentReference[oaicite:0]{index=0}  

---

### 2. Creating a Pydantic Model

Example:

```python
from pydantic import BaseModel, Field

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    tags: list[str] = []
```
- Field() is used for validation
- You can define limits and defaults

---

###  3. Using Model in Query Parameters
```python
@app.get("/items/")
async def read_items(filters: FilterParams = Query()):
```
FastAPI:

- reads query parameters
- maps them into the model
- validates everything automatically

---

### 4. Annotated (Recommended Way)

Modern approach:

```python
from typing import Annotated

filters: Annotated[FilterParams, Query()]
```

---

### 5. Restricting Extra Parameters

You can forbid unexpected query parameters:

```python
class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
```
- If user sends unknown parameter → error
- Helps keep API strict and predictable

---

## Key Takeaways
- Query parameters can be grouped into Pydantic models
- Reduces code duplication
- Centralizes validation
- Supports strict control over input
- Makes APIs cleaner and scalable