from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


# Basic validation
@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=20)] = None
):
    return {"q": q}


# Required parameter
@app.get("/search/")
async def search(q: Annotated[str, Query(min_length=3)]):
    return {"query": q}


# Regex validation
@app.get("/filter/")
async def filter_items(
    q: Annotated[str | None, Query(pattern="^prod")] = None
):
    return {"filter": q}


# Multiple values
@app.get("/tags/")
async def get_tags(
    q: Annotated[list[str], Query()] = []
):
    return {"tags": q}


# Metadata example
@app.get("/products/")
async def get_products(
    q: Annotated[
        str | None,
        Query(
            title="Search parameter",
            description="Used to filter products",
            min_length=2
        )
    ] = None
):
    return {"search": q}


# Deprecated parameter
@app.get("/old-endpoint/")
async def old(q: Annotated[str | None, Query(deprecated=True)] = None):
    return {"q": q}
