# FastAPI Path Parameters Practice

## Overview
This project is based on the official FastAPI tutorial about path parameters.  
The goal was to understand how to create dynamic routes and work with values passed directly in the URL.

---

### 1. Path Parameters Concept (task_1.py)
Path parameters are variables included directly in the URL.

Example:

```bash
/product/10
```

They are used to:
- access specific data (like product by ID)
- avoid creating multiple endpoints
- make APIs more flexible  

---

### 2. Dynamic Routing
Instead of writing multiple routes:

```bash
/product1
/product2
/product3
```


We can define one dynamic route:
```python
@app.get("/products/{product_id}")
```
This allows one endpoint to handle multiple inputs.

---

## Enum (Predefined Values)(task_2.py)

## FastAPI allows restricting path parameters to a fixed set of values using Enum.

Example:

```python
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
```
Using it in a route:

```python
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}
```

## Behavior:

- Only predefined values are allowed
- Invalid values will automatically return an error
- Useful for controlled inputs (e.g., categories, model names, statuses)

---

## Key Takeaways
- Path parameters make APIs dynamic
- They are required and part of the URL
- FastAPI automatically validates and converts data types
- Enum helps restrict allowed values
- One route can replace many static endpoints