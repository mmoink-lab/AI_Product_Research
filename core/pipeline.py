"""
BD Product Intelligence Pipeline v1
"""

from intelligence.product_classifier import ProductClassifier
from intelligence.scoring_engine import ProductScoringEngine


class ProductPipeline:

    def __init__(self):

        self.classifier = ProductClassifier()
        self.scoring = ProductScoringEngine()

    def process(self, products):

        results = []

        for product in products:

            row = self.classifier.classify(
                product["product_name"]
            )

            score = self.scoring.analyze(
                row["fingerprint"]
            )

            results.append({

                "product_name": product["product_name"],

                "price": product.get("price", 0),

                "fingerprint": row["fingerprint"],

                "main_category": row["main_category"],

                "sub_category": row["sub_category"],

                "product_type": row["product_type"],

                "demand_score": score["demand_score"],

                "competition_score": score["competition_score"],

                "profit_score": score["profit_score"],

                "shipping_score": score["shipping_score"],

                "winner_score": score["winner_score"]

            })

        return results