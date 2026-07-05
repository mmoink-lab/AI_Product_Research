from database.market_repository import MarketRepository

from intelligence.saturation_engine import SaturationEngine

products = MarketRepository().load_products()

engine = SaturationEngine()

results = engine.analyze(products)

print("=" * 80)

for item in results:

    print(

        item["family"],

        "| Listings:",

        item["listings"],

        "| Saturation:",

        item["saturation_score"]

    )