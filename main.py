import time
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
db = []


class Currency(BaseModel):
    name: str
    value: float


@app.get("/")
def index():
    return {'key': 'value'}


@app.get('/currency')
def get_currency():
    results = []
    for currency in db:
        r = requests.get(f'https://v6.exchangerate-api.com/v6/786cc711780443f0973ae997/latest/{currency["currencyName"]}')
        current_currency = r.json()['currency']
        print(r.json())
        results.append({'name': currency['name'], 'value': currency['value ']})
    return results


@app.get('/currency/{currency_id}')
def get_currency(currency_id: int):
    return db[currency_id - 1]


@app.post('/currency')
def create_currency(currency: Currency):  # create currency object
    db.append(currency.dict())  # convert it to dict
    return db[-1]  # return last object from db list


@app.delete('/currency/{currency_id}')
def delete_currency(currency_id: int):
    db.pop(currency_id - 1)
    return {}