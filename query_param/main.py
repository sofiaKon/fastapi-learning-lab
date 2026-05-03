from fastapi import FastAPI

app = FastAPI()


# Basic query parameters example
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "message": "Items list with pagination"
    }


# Required query parameter
@app.get("/search/")
async def search_item(q: str):
    return {
        "query": q,
        "result": "Search completed"
    }


# Boolean query parameter
@app.get("/products/")
async def get_products(short: bool = False):
    if short:
        return {"message": "Short product list"}
    return {"message": "Full product description list"}


# Combined path + query parameters
@app.get("/users/{user_id}/orders/{order_id}")
async def get_order(user_id: int, order_id: int, detail: bool = False):
    return {
        "user_id": user_id,
        "order_id": order_id,
        "detail": detail
    }
