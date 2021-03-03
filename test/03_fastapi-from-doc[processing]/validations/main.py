from typing import List,Optional
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Optional[str] = Query(
    ...,min_length=3, max_length=50, regex="^fixedquery$"
    )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# q is not required
# can set the min or max length
# also can set the regular expression

@app.get("/users/")
async def read_users(q: Optional[List[str]] = Query(None)):
    query_users = {"q" : q}
    return query_users
