"""
First app to test fastapi
"""

from fastapi import FastAPI

app = FastAPI()


# Create a route
@app.get("/")
def read_root():
    return {"message": "Hello World"}
