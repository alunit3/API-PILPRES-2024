
from fastapi import FastAPI
from api import sirekap
import asyncio

app = FastAPI()


@app.get("/all")
def all_data():
    return asyncio.run(sirekap.get_data())
