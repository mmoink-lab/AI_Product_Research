from database.market_repository import MarketRepository

from intelligence.competition_engine import CompetitionEngine


products = MarketRepository().load_products()

engine = CompetitionEngine()

results = engine.analyze(products)

print("=" * 80)

for item in results:

    print(

        item["family"],

        "| Listings:",

        item["listings"],

        "| Sold:",

        item["sold"],

        "| Ratio:",

        item["ratio"],

        "| Competition:",

        item["competition_score"]

    )