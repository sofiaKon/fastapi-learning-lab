# FastAPI Path Parameters Numeric Validation Practice

## Overview
This project is based on the official FastAPI tutorial about path parameter validations.  
The goal was to understand how to restrict and validate numeric values directly in the URL.

---

### 1. Advanced Path Parameters
FastAPI allows adding validation rules to path parameters using `Path()`.

Example:
```python
from fastapi import Path
```
---

### 2. Using Path() for Validation

You can define constraints for numeric values:
```python
item_id: int = Path(ge=1)
```
This means:

- value must be ≥ 1
- 0 or negative numbers are not allowed

---

### 3. Numeric Constraints

FastAPI provides built-in validation rules:

ge → greater than or equal (≥)
gt → greater than (>)
le → less than or equal (≤)
lt → less than (<)

Example:

```python
item_id: int = Path(ge=1, le=1000)
```
allowed range: 1 to 1000

---

###  4. Automatic Validation

FastAPI automatically checks values:

valid → request works
invalid → error 422

Example:

```bash
/items/10   ✔ valid
/items/0    ✖ invalid
/items/-5   ✖ invalid
```

---

### 5. Metadata for Documentation

You can add extra information:
```python 
item_id: int = Path(
    title="Item ID",
    description="The ID of the product",
    ge=1
)
```

---

### 6. Combining with Query Parameters

You can use both:
```python 
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(ge=1),
    q: str = None
):
```
FastAPI automatically distinguishes them.

---

## Key Takeaways
- Path() adds validation and metadata
- You can control numeric ranges directly in URL
- FastAPI automatically validates input
- Invalid values return clear errors
- Helps build safer and more predictable APIs

