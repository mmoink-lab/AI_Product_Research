from database.market_repository import MarketRepository
from intelligence.family_price_analyzer import FamilyPriceAnalyzer
from core.family_detector import ProductFamilyDetector


repo = MarketRepository()

products = repo.load_products()

# Family Assign
for item in products:
    item["family"] = ProductFamilyDetector.get_family_name(
        item["product"]
    )

engine = FamilyPriceAnalyzer()

results = engine.analyze(products)

print("=" * 70)

for row in results:

    print(
        row["family"],
        "| Count:", row["count"],
        "| Avg:", row["average"],
        "| Low:", row["lowest"],
        "| High:", row["highest"]
    )