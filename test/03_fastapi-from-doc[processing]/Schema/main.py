from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
    class Config:
        schema_extra = {
            "example" : {
                "name" : "Foo",
                "description": "A very nice item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
        
class User(BaseModel):
    name: str = Field(..., example="User1")
    description: Optional[str] = Field(None, example= "A very nice User")


class Method(BaseModel):
    name: str
    description: Optional[str] = None
    method_id : int
        
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    results = {"user_id": user_id, "user": user}
    return results

@app.put("/methods/{method_id}")
async def update_method(method_id:int, method: Method = Body(...,
                                                             example={
                                                                 "name": "Method1",
                                                                 "description": "A very nice method",
                                                                 "method_id": 1,
                                                             })):
    results = {"method_id": method_id, "method": method}
    return results

# No validation!