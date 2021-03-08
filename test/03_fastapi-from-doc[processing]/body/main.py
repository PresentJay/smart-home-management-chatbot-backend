from typing import Optional, List, Set

from fastapi import FastAPI, Path
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(
        ..., gt=0, description="The price must be greater than zero."
    )
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[Image] = None
    images: Optional[List[Image]] = None
    
class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id:int,
    item: Item = Body(..., embed=True),
    user: User,
    importance: int = Body(..., gt=0), # required
    q: Optional[str] = None
):
    results = {"item_id" : item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results