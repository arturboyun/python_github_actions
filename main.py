from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/sum")
async def read_root(a: Union[int, float], b: Union[int, float]):
    return {"sum": a + b}
