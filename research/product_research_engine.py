"""
BD Product Intelligence
Product Research Engine v2
"""

from core.pipeline import ProductPipeline
from research.price_intelligence import PriceIntelligence
from research.demand_engine import DemandEngine


class ProductResearchEngine:

    def __init__(self):

        self.pipeline = ProductPipeline()
        self.price = PriceIntelligence()
        self.demand = DemandEngine()

    def run(self, products):

        results = self.pipeline.process(products)

        price_report = self.price.analyze(results)

        demand_report = self.demand.analyze(results)

        final = []

        for item in results:

            fp = item["fingerprint"]

            price = price_report.get(fp, {})

            demand = demand_report.get(fp, {})

            item.update(price)

            item.update(demand)

            item["winner_score"] = round(

                item["winner_score"] * 0.5 +

                item["demand_score"] * 0.3 +

                (100 - item["competition_score"]) * 0.2

            )

            final.append(item)

        final.sort(

            key=lambda x: x["winner_score"],

            reverse=True

        )

        return final

    def top_winners(self, products, limit=100):

        return self.run(products)[:limit]