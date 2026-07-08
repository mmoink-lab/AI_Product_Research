import requests

url = "https://www.daraz.com.bd/catalog/"

params = {
    "ajax": "true",
    "isFirstRequest": "true",
    "page": 1,
    "q": "usb blender"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=30
)

print("=" * 80)

print(r.status_code)

print(r.headers.get("content-type"))

print()

print(r.text[:1000])

print()

print("=" * 80)