from collections import defaultdict


class TopSellingEngine:

    def analyze(self, products):

        family_sales = defaultdict(int)

        for item in products:

            family = item.get("family", "").strip()

            if not family:
                continue

            sold = item.get("sold_count", 0)

            try:
                sold = int(sold)
            except:
                sold = 0

            family_sales[family] += sold

        total_market_sales = sum(family_sales.values())

        if total_market_sales == 0:
            total_market_sales = 1

        results = []

        for family, sold in family_sales.items():

            score = round(
                (sold / total_market_sales) * 100,
                2
            )

            results.append({

                "family": family,
                "total_sold": sold,
                "top_selling_score": score

            })

        results.sort(
            key=lambda x: x["top_selling_score"],
            reverse=True
        )

        return results