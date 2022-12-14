import pytest
import main
import json
import requests

@pytest.mark.prod_exchange
def test_get_all_currency():
    response = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=36d4d7b23910dc84442f4bc147637fab').json()
    get_rates = response["rates"]
    currency_list = list(k for k, v in get_rates.items() if v >= 10)
    nice_formatted_currency_list = json.dumps(currency_list, indent=4)
    list_from_main = main.get_all_currency()
    assert nice_formatted_currency_list not in list_from_main
