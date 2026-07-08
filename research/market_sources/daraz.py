"""
Daraz Marketplace Provider
"""

import requests

from research.market_sources.provider import MarketplaceProvider


class DarazProvider(MarketplaceProvider):

    name = "Daraz"

    URL = "https://www.daraz.com.bd/catalog/"

    def search(self, query):

        r = requests.get(
            self.URL,
            params={
                "ajax": "true",
                "isFirstRequest": "true",
                "page": 1,
                "q": query,
            },
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30,
        )

        data = r.json()

        items = data.get("mods", {}).get("listItems", [])

        results = []

        for item in items:

            url = item.get("itemUrl", "")

            if url.startswith("//"):
                url = "https:" + url

            results.append(
                {
                    "marketplace": "Daraz",
                    "title": item.get("name", ""),
                    "price": float(item.get("price", 0)),
                    "original_price": float(item.get("originalPrice", 0))
                    if item.get("originalPrice")
                    else 0,
                    "discount": item.get("discount", ""),
                    "rating": float(item.get("ratingScore") or 0),
                    "review_count": int(item.get("review") or 0),
                    "sold": item.get("itemSoldCntShow", ""),
                    "seller": item.get("sellerName", ""),
                    "brand": item.get("brandName", ""),
                    "location": item.get("location", ""),
                    "image": item.get("image", ""),
                    "url": url,
                }
            )

        return results