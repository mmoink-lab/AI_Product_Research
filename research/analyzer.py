"""
Research Analyzer
"""

from collections import Counter


class Analyzer:

    def summary(self, products):

        fingerprints = Counter()

        categories = Counter()

        winner_scores = []

        for item in products:

            fingerprints[item["fingerprint"]] += 1

            categories[item["main_category"]] += 1

            winner_scores.append(item["winner_score"])

        return {

            "total_products": len(products),

            "unique_fingerprints": len(fingerprints),

            "top_fingerprints": fingerprints.most_common(20),

            "top_categories": categories.most_common(),

            "average_winner_score":

                round(sum(winner_scores) / len(winner_scores), 2)

                if winner_scores else 0

        }