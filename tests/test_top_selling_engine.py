from database.market_repository import MarketRepository
from intelligence.top_selling_engine import TopSellingEngine

products = MarketRepository().load_products()

results = TopSellingEngine().analyze(products)

print("=" * 70)

for item in results:

    print(

        item["family"],
        "|",
        item["total_sold"],
        "|",
        item["top_selling_score"]

    )