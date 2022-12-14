import time
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from pydantic import BaseModel

app = FastAPI()
db = []


class Currency(BaseModel):
    name: str
    value: float


@app.get("/")
def index():
    return {'key': 'value'}


@app.post('/currency')
def create_currency(currency: Currency):  # create currency object
    db.append(currency.dict())  # convert it to dict
    return db[-1]  # return last object from db list


@app.get('/currency/{currency_id}')
def get_currency_by_id(currency_id: int):
    return db[currency_id - 1]


@app.get ('/currency/')
def get_all_currency():
    return db


@app.delete('/currency/{currency_id}')
def delete_currency(currency_id: int):
    db.pop(currency_id - 1)
    return {}
