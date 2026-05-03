from fastapi import FastAPI, Path

app = FastAPI()


# Basic numeric validation
@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(ge=1)):
    return {"item_id": item_id}


# Range validation
@app.get("/products/{product_id}")
async def get_product(
    product_id: int = Path(ge=1, le=1000)
):
    return {"product_id": product_id}


# With metadata
@app.get("/orders/{order_id}")
async def get_order(
    order_id: int = Path(
        title="Order ID",
        description="ID must be between 1 and 500",
        ge=1,
        le=500
    )
):
    return {"order_id": order_id}


# Combined with query parameter
@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(ge=1),
    detail: bool = False
):
    return {
        "user_id": user_id,
        "detail": detail
    }
