import requests
from pprint import pprint

r = requests.get(
    "https://www.daraz.com.bd/catalog/",
    params={
        "ajax": "true",
        "isFirstRequest": "true",
        "page": 1,
        "q": "usb blender"
    },
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

data = r.json()

item = data["mods"]["listItems"][0]

print("=" * 100)

print(item.keys())

print("=" * 100)

pprint(item)

print("=" * 100)