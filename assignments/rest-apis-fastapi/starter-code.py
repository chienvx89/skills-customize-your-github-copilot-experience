from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO: Define a Pydantic model for your resource
# Example: class Item(BaseModel):
#            id: int
#            name: str
#            description: str = None


# Sample in-memory storage (for demonstration)
items_db = []


# TODO: Create a GET endpoint that returns all items
# @app.get("/items")
# async def get_all_items():


# TODO: Create a GET endpoint that returns a single item by ID
# @app.get("/items/{item_id}")
# async def get_item(item_id: int):


# TODO: Create a POST endpoint to add a new item
# @app.post("/items")
# async def create_item(item: Item):


# TODO: Create a PUT endpoint to update an item
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):


# TODO: Create a DELETE endpoint to remove an item
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
