"""
First app to test fastapi
"""

from fastapi import FastAPI

app = FastAPI()


# Create a route
@app.get("/")
def read_root():
    return {"message": "Welcome User!"}


@app.get("/divide")
def divide(a: int, b: int):
    return {"result": a / b}


@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}


@app.get("subtract")
def subtract(a: int, b: int):
    return {"result": a - b}
