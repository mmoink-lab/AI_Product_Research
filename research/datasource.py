"""
Data Source Engine v1
"""


class DataSource:

    def __init__(self):

        self.records = []

    def load(self, products):

        self.records = products

    def all(self):

        return self.records

    def total_products(self):

        return len(self.records)

    def unique_families(self):

        families = set()

        for item in self.records:

            fp = item.get("fingerprint")

            if fp:
                families.add(fp)

        return len(families)

    def filter_by_fingerprint(self, fingerprint):

        result = []

        for item in self.records:

            if item.get("fingerprint") == fingerprint:
                result.append(item)

        return result

    def average_price(self, fingerprint):

        items = self.filter_by_fingerprint(fingerprint)

        prices = []

        for item in items:

            price = item.get("price")

            if isinstance(price, (int, float)):
                prices.append(price)

        if not prices:
            return 0

        return round(sum(prices) / len(prices), 2)

    def lowest_price(self, fingerprint):

        items = self.filter_by_fingerprint(fingerprint)

        prices = []

        for item in items:

            price = item.get("price")

            if isinstance(price, (int, float)):
                prices.append(price)

        if not prices:
            return 0

        return min(prices)

    def highest_price(self, fingerprint):

        items = self.filter_by_fingerprint(fingerprint)

        prices = []

        for item in items:

            price = item.get("price")

            if isinstance(price, (int, float)):
                prices.append(price)

        if not prices:
            return 0

        return max(prices)