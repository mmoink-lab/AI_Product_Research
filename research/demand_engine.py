"""
Demand Intelligence Engine v1
"""


class DemandEngine:

    def analyze(self, products):

        counts = {}

        for product in products:

            fp = product["fingerprint"]

            counts[fp] = counts.get(fp, 0) + 1

        if not counts:
            return {}

        max_count = max(counts.values())

        report = {}

        for fp, count in counts.items():

            demand_score = round((count / max_count) * 100)

            competition_score = min(100, count * 5)

            report[fp] = {

                "total_products": count,

                "demand_score": demand_score,

                "competition_score": competition_score

            }

        return report