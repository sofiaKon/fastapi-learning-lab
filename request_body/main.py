from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic model
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# Create product
@app.post("/products/")
async def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }


# Update product with path + body
@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    return {
        "product_id": product_id,
        "updated_data": product
    }


# Simple GET
@app.get("/")
async def root():
    return {"message": "Request body example is running"}
