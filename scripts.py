from pprint import pprint

import requests
from furl import furl

url = furl('https://api.food.ru/content/v2')

response = requests.get(
    url / 'search',
    params={
        'query': 'борщ',
        'format': 'json',
        'page': 1,
        'max_per_page': 20,
        'material': ['recipe', 'product', 'news']
    },
    headers={'Accept': 'application/json', 'Content-Type': 'application/json'}
)

print(response)
pprint(response.json())
