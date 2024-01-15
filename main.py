from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Response": {"Message": "This is the Message from Root"}}
