from core.feature_extractor import FeatureExtractor
from intelligence.product_matcher import ProductMatcher
from intelligence.final_match_score import FinalMatchScore


class BDMarketEngine:

    def __init__(self):

        self.extractor = FeatureExtractor()
        self.matcher = ProductMatcher()
        self.final = FinalMatchScore()

    def analyze(self, supplier_product, market_products):

        supplier = self.extractor.extract(
            supplier_product
        )

        results = []

        total = len(market_products)

        for position, item in enumerate(market_products):

            market = self.extractor.extract(
                item["product"]
            )

            feature_score = self.matcher.match(
                supplier,
                market
            )

            name_score = self.matcher.fuzzy_score(
                supplier_product,
                item["product"]
            )

            final_score = self.final.calculate(
                feature_score,
                name_score,
                position,
                total
            )

            results.append({

                "product": item["product"],

                "price": item["price"],

                "score": final_score

            })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results