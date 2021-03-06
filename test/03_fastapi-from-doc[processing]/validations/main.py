from typing import List,Optional
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(
    ...,
    title= "Query String",
    description= "Query string for the items to search in the database that have a good match",
    min_length=3, max_length=50, regex="^fixedquery$",
    deprecated=True
    )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# q is not required
# can set the min or max length
# also can set the regular expression

# metadata title, description

@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000),
        q: Optional[str] = Query(None, alias="item-query")
):    
    results = {"item_id" : item_id}
    if q:
        results.update(y)({"q": q})
        
    return results

# first parameter * makes like kwargs.
# following parameters should be consist of key-value.

# gt : greater than
# ge : greater than or equal
# lt : less than
# lt : less than or equal

@app.get("/users/")
async def read_users(q: Optional[List[str]] = Query(None, alias="user-query")):
    query_users = {"q" : q}
    return query_users

# List[str] checks in List, and validate that members are str type
# but just list wouldn't.

# alias enable request like this => /items/?item-query=foobaritems
# instead of => /items/?q=foobaritems

