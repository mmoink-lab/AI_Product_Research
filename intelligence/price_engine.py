from statistics import mean
from statistics import median


class PriceEngine:

    def analyze(self, products):

        families = {}

        for item in products:

            family = item["family"]

            families.setdefault(

                family,

                []

            ).append(

                item["price"]

            )

        results = []

        for family, prices in families.items():

            prices = sorted(prices)

            lowest = min(prices)

            highest = max(prices)

            avg = round(

                mean(prices),

                2

            )

            med = round(

                median(prices),

                2

            )

            if avg <= 700:

                segment = "Budget"

            elif avg <= 1200:

                segment = "Mass Market"

            else:

                segment = "Premium"

            results.append({

                "family": family,

                "lowest": lowest,

                "average": avg,

                "median": med,

                "highest": highest,

                "segment": segment

            })

        return results