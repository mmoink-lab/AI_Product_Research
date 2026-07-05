from database.market_repository import MarketRepository
from intelligence.price_engine import PriceEngine

products = MarketRepository().load_products()

engine = PriceEngine()

results = engine.analyze(

    products

)

print("=" * 100)

for item in results:

    print(item["family"])

    print(

        "Lowest :", item["lowest"]

    )

    print(

        "Average:", item["average"]

    )

    print(

        "Median :", item["median"]

    )

    print(

        "Highest:", item["highest"]

    )

    print(

        "Segment:", item["segment"]

    )

    print("-" * 100)