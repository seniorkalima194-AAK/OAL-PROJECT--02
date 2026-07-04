from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
items_db = {
    1: {"name": "laptop","price":9000 },
    2: {"name": "phone","price":3500}
}

class Item(BaseModel):
    name: str
    price: float

@app.get("/items")
async def get_items():
    return items_db

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id in items_db:
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
async def create_item(item: Item):
    item_id = max(items_db.keys()) + 1
    items_db[item_id] = item.model_dump()
    return items_db[item_id]
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id in items_db:
        items_db[item_id] = item.model_dump()
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")