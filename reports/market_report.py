from database.market_repository import MarketRepository
from core.family_detector import ProductFamilyDetector
from intelligence.family_price_analyzer import FamilyPriceAnalyzer
from intelligence.top_selling_engine import TopSellingEngine
from intelligence.opportunity_engine import OpportunityEngine


repo = MarketRepository()

products = repo.load_products()

# Detect Family
for item in products:

    item["family"] = ProductFamilyDetector.get_family_name(
        item["product"]
    )


# Top Selling
top_engine = TopSellingEngine()

top_results = top_engine.analyze(products)


# Price Analysis
price_engine = FamilyPriceAnalyzer()

price_results = price_engine.analyze(products)


# Convert to dictionary
price_map = {}

for item in price_results:

    price_map[item["family"]] = item


# Opportunity Score
opp_engine = OpportunityEngine()


print("=" * 90)
print("BANGLADESH MARKET REPORT")
print("=" * 90)

for row in top_results:

    family = row["family"]

    price = price_map.get(family)

    score = opp_engine.calculate(
        row["score"],
        price["average"]
    )

    print(f"Family           : {family}")
    print(f"Products Found   : {row['products']}")
    print(f"Market Share     : {row['score']}%")
    print(f"Average Price    : ?{price['average']}")
    print(f"Lowest Price     : ?{price['lowest']}")
    print(f"Highest Price    : ?{price['highest']}")
    print(f"Opportunity      : {score}")

    print("-" * 90)