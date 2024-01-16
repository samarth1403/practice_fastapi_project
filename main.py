from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"Response": {"Message": "This is the Message from Root"}}

# Path Parameter


@app.get("/root/{id}")
def read_path_parameter(id: int):
    return {"Path Parameter": id}


# Query Parameter
@app.get("/query")
def read_query_parameter(limit: int, offset: Optional[int] = 0):
    query_list = {}
    if limit is not 0:
        query_list.update({"limit": limit})
    if offset is not 0:
        query_list.update({"offset": offset})
    return query_list


# Request Body
class User(BaseModel):
    name: str
    age: int
    gender: str


@app.post("/user/create")
def create_user(user: User):
    return {"UserInfo": user}
