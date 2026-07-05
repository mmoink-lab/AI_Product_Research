from collections import defaultdict


class FamilyPriceAnalyzer:

    def analyze(self, products):

        families = defaultdict(list)

        for item in products:

            family = item["family"]

            if not family:
                continue

            families[family].append(item["price"])

        results = []

        for family, prices in families.items():

            results.append({

                "family": family,

                "lowest": min(prices),

                "highest": max(prices),

                "average": round(sum(prices) / len(prices), 2),

                "count": len(prices)

            })

        results.sort(
            key=lambda x: x["count"],
            reverse=True
        )

        return results