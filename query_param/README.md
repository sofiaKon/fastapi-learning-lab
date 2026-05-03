# FastAPI Query Parameters Practice

## Overview
This project is based on the official FastAPI tutorial about query parameters.  
The goal was to understand how to pass additional data through the URL and control API behavior.

---

### 1. What Are Query Parameters
Query parameters are values passed in the URL after `?`.

Example:

```bash
/items/?skip=0&limit=10
```


They are used to:
- filter data  
- control output  
- customize requests without changing the endpoint :contentReference[oaicite:0]{index=0}  

---

### 2. How FastAPI Detects Query Parameters
If a parameter is **not part of the path**, FastAPI automatically treats it as a query parameter. :contentReference[oaicite:1]{index=1}  

Example:
```python
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
```

---

### 3.Default Values (Optional Parameters)

If a parameter has a default value → it becomes optional.

- If not provided → default value is used
- Makes endpoints flexible

---

### 4. Required Query Parameters

If no default value is provided → parameter is required.

```python 
async def read_item(item_id: str, q: str):
```
If missing → FastAPI returns an error (422)

---

### 5. Boolean Parameters

FastAPI automatically converts values to bool.

Examples that become True:
```bash
?short=true
?short=1
?short=yes
```
FastAPI handles multiple formats automatically

---

### 6. Multiple Parameters (path parameters + query parameters)

```python
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str = None):
```
FastAPI distinguishes them automatically by name

---

## Key Takeaways
- Query parameters appear after ? in URL
- They are optional by default (if value is provided)
- FastAPI automatically validates and converts types
- Required parameters have no default value
- They make APIs flexible without creating new routes

