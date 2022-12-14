import time
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json

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


@app.get('/currency')
def get_all_currency():
    api_call = requests.get(
        'https://v6.exchangerate-api.com/v6/786cc711780443f0973ae997/latest/USD').json()  # no spaces, http and not https
    get_rates = api_call['rates']
    currency_list = list(k for k, v in get_rates.items() if v < 10)
    return json.dumps(currency_list, indent=4)

    return db

def dev_exchange(): #this function generate json file (one time only) with the api data
    currency_names = []
    api_call = requests.get('https://v6.exchangerate-api.com/v6/786cc711780443f0973ae997/latest/USD').json()
    with open('all_currency_file_new.json', 'w') as outfile:
        json.dump(api_call, outfile, indent=4)

#dev_exchange()


@app.delete('/currency/{currency_id}')
def delete_currency(currency_id: int):
    db.pop(currency_id - 1)
    return {}
