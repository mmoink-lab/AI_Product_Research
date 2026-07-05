from collections import Counter


class BestSellingAnalyzer:

    def analyze(self, products):

        families = []

        for product in products:

            family = product.get("family")

            if family:
                families.append(family)

        counter = Counter(families)

        result = []

        total = len(families)

        for family, count in counter.most_common():

            score = round((count / total) * 100, 2)

            result.append({

                "family": family,

                "products_found": count,

                "best_selling_score": score

            })

        return result