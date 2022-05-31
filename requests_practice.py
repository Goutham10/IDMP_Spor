import requests

url = ("https://spor.ema.europa.eu/v1/lists?pagesize=500")

data = {
    "lang": "en",
    "page": "1",
    "pagesize": "20",
    "parent": "all",
    "sortby": "id",
}



