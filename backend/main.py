from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Next.js + FastAPI Backend")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

# Example data
items = [
    Item(id=1, name="Item 1", description="Description for Item 1"),
    Item(id=2, name="Item 2", description="Description for Item 2"),
]

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI backend!"}

@app.get("/api/items", response_model=List[Item])
async def get_items():
    return items

@app.get("/api/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"} 