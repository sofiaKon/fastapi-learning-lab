# FastAPI Request Body Practice

## Overview
This project is based on the official FastAPI tutorial about request bodies.  
The goal was to understand how to send and receive structured data using JSON and Pydantic models.

---

## What I Learned

### 1. What Is a Request Body
A request body is data sent by the client to the API, usually in JSON format.

Example:
```json
{
  "name": "Laptop",
  "price": 1200,
  "in_stock": true
}
```
---

### 2. Using Pydantic Models

FastAPI uses Pydantic to define and validate request data.

Example:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
```

---

### 3. Receiving Data in API

The model is used as a parameter in the endpoint:
```python
@app.post("/items/")
async def create_item(item: Item):
```
FastAPI automatically:

- reads JSON body
- validates data
- converts types

---

### 4. Automatic Validation

If the data is incorrect:

- missing fields
- wrong types

FastAPI returns an error (422) automatically.

---

## Key Takeaways
- Request body is used to send JSON data
- Pydantic models define structure and validation
- FastAPI automatically parses and validates input
- Default values make fields optional