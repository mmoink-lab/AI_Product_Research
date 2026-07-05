from collections import defaultdict


class SellerCounterEngine:

    def analyze(self, products):

        families = defaultdict(set)

        for item in products:

            family = item.get("family", "").strip()

            seller = item.get("shop_name", "").strip()

            if not family:
                continue

            if seller:

                families[family].add(seller)

        results = []

        for family, sellers in families.items():

            results.append({

                "family": family,

                "seller_count": len(sellers)

            })

        return results