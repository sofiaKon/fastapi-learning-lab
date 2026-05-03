from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


# Pydantic model for query parameters
class ProductFilter(BaseModel):
    limit: int = Field(10, gt=0, le=50)
    offset: int = Field(0, ge=0)
    category: str | None = None
    tags: list[str] = []

    model_config = {"extra": "forbid"}


# Using query parameter model
@app.get("/products/")
async def get_products(
    filters: Annotated[ProductFilter, Query()]
):
    return {
        "filters": filters
    }


# Simple root
@app.get("/")
async def root():
    return {"message": "Query model example is running"}
