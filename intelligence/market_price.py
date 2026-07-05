class MarketPriceAnalyzer:

    def analyze(self, products):

        prices = []

        for item in products:

            price = item.get("price")

            if isinstance(price, (int, float)):
                prices.append(price)

        if len(prices) == 0:

            return {
                "lowest_price": None,
                "highest_price": None,
                "average_price": None
            }

        average = round(sum(prices) / len(prices), 2)

        return {
            "lowest_price": min(prices),
            "highest_price": max(prices),
            "average_price": average
        }