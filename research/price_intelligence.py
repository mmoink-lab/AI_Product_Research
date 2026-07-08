"""
Price Intelligence Engine v1
"""

from statistics import median


class PriceIntelligence:

    def analyze(self, products):

        groups = {}

        for product in products:

            fp = product["fingerprint"]

            price = product.get("price", 0)

            try:
                price = float(price)
            except Exception:
                price = 0

            groups.setdefault(fp, []).append(price)

        report = {}

        for fp, prices in groups.items():

            prices = sorted([p for p in prices if p > 0])

            if not prices:

                report[fp] = {
                    "lowest_price": 0,
                    "highest_price": 0,
                    "average_price": 0,
                    "median_price": 0,
                    "price_range": 0,
                    "price_spread_percent": 0
                }

                continue

            low = min(prices)
            high = max(prices)
            avg = round(sum(prices) / len(prices), 2)
            med = round(median(prices), 2)
            rng = high - low

            spread = 0

            if avg > 0:
                spread = round((rng / avg) * 100, 2)

            report[fp] = {

                "lowest_price": low,

                "highest_price": high,

                "average_price": avg,

                "median_price": med,

                "price_range": rng,

                "price_spread_percent": spread

            }

        return report