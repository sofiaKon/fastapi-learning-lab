# FastAPI Query Parameters Validation Practice

## Overview
This project is based on the official FastAPI tutorial about query parameter validations.  
The goal was to learn how to control and validate user input using built-in tools like `Query` and `Annotated`.

---

### 1. Advanced Query Parameters
FastAPI allows adding validation rules to query parameters.

Example:
```python
from fastapi import Query
```

---

### 2. Using Query() for Validation

You can define rules directly in the parameter:
```python
q: str = Query(default=None, min_length=3, max_length=50)
```
This means:

- minimum length = 3
- maximum length = 50

---

### 3. Required Parameters

To make a query parameter required:

```python
q: str = Query(...)
```
- ... means no default value
- FastAPI will raise an error if missing

---

### 4. Regex (Pattern Validation)

You can restrict format using patterns:

```python
q: str = Query(pattern="^item")
```
- ust start with "item"
- useful for strict input control

---

### 5. Multiple Values (List Parameters)

Query parameters can accept lists:

```python
q: list[str] = Query(default=[])
```
Example:

```bash
/items/?q=apple&q=banana
```

---

### 6. Metadata (Descriptions, Titles)

You can add extra info for documentation:

```python
q: str = Query(
    default=None,
    title="Search query",
    description="Search term for filtering products"
)
```

---

### 7. Deprecated Parameters

You can mark parameters as deprecated:
```python
q: str = Query(default=None, deprecated=True)
```
- still works
- but marked as outdated in docs

---

## Key Takeaways
- Query() allows strict validation of user input
- You can control length, format, and requirements
- Supports lists and metadata
- Annotated is the modern way to write clean code
- Improves API reliability and documentation