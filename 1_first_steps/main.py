from fastapi import FastAPI

# Create FastAPI application instance
app = FastAPI()

# When a GET request is sent to "/", this function runs


@app.get("/")
async def root():
    return {"message": "Welcome to our online store API"}


# Path parameter example
# Allows passing values directly in the URL (e.g., /items/10)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "status": "Item retrieved successfully"}


# Multiple HTTP method examples
# POST: create a new item
@app.post("/items/")
async def create_item():
    return {"message": "New product has been added to inventory"}


# PUT: update existing item
@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"message": f"Product with ID {item_id} has been updated"}


# DELETE: remove item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Product with ID {item_id} has been removed"}


# async vs sync example
@app.get("/sync-example")
def sync_example():
    return {"message": "This is a synchronous endpoint example"}
