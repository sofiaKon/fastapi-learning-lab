from fastapi import FastAPI

app = FastAPI()


# Root endpoint
@app.get("/")
async def home():
    return {"message": "API is running"}


# Example of path parameter
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id,
        "info": "Product data successfully retrieved"
    }


# Another example
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "status": "User profile loaded"
    }
