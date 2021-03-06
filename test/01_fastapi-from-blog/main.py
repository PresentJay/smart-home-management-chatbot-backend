from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

# @app.get("/")
# async def root():
#     return { "message" : "Hello World!" }

@app.get("/items/")
async def create_item(item: Item):
    return item