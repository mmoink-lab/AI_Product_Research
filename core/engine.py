"""
BD Product Intelligence Engine
Production v2
"""

from core.pipeline import ProductPipeline
from research.price_intelligence import PriceIntelligence
from research.demand_engine import DemandEngine
from intelligence.ranking_engine import RankingEngine


class ProductEngine:

    def __init__(self):

        self.pipeline = ProductPipeline()

        self.price = PriceIntelligence()

        self.demand = DemandEngine()

        self.ranking = RankingEngine()

    def run(self, products):

        processed = self.pipeline.process(products)

        price_report = self.price.analyze(processed)

        demand_report = self.demand.analyze(processed)

        final = []

        for item in processed:

            fp = item["fingerprint"]

            row = dict(item)

            row.update(price_report.get(fp, {}))

            row.update(demand_report.get(fp, {}))

            final.append(row)

        return self.ranking.calculate(final)