from database.market_repository import MarketRepository

from intelligence.demand_engine import DemandEngine


products = MarketRepository().load_products()

engine = DemandEngine()

results = engine.analyze(products)

print("=" * 100)

for item in results:

    print(

        item["family"],

        "| Listings:",

        item["listings"],

        "| Sold:",

        item["sold"],

        "| Avg:",

        item["average_sold"],

        "| Demand:",

        item["demand"]

    )