from typing import Optional
from enum import Enum
# Enumarations are available in python since version 3.4


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [ {"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item):
    return {"item_name": item.name, "item_id": item.id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deel Learning FTW!"} # For The Win!
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"} # residual - 잔차