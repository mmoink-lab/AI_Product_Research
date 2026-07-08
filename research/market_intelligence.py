from research.market_sources.daraz import DarazProvider


class MarketIntelligence:

    def __init__(self):

        self.provider = DarazProvider()

    def analyze(self, fingerprint):

        products = self.provider.search(fingerprint)

        if not products:

            return None

        prices = [
            p["price"]
            for p in products
            if p["price"] > 0
        ]

        if not prices:

            return None

        return {

            "fingerprint": fingerprint,

            "marketplace": "Daraz",

            "products_found": len(products),

            "lowest_price": min(prices),

            "highest_price": max(prices),

            "average_price": round(sum(prices) / len(prices), 2),

            "top_product": products[0]["title"],

            "top_seller": products[0]["seller"],

            "top_url": products[0]["url"]

        }