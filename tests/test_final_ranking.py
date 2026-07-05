from database.market_repository import MarketRepository
from intelligence.final_ranking_engine import FinalRankingEngine

engine = FinalRankingEngine()

products = MarketRepository().load_products()

families = {}

for item in products:

    family = item["family"]

    if family not in families:

        families[family] = item


print("=" * 80)

for family, item in families.items():

    score = engine.calculate(

        item["top_selling_score"],

        item["evergreen_score"],

        item["seasonal_score"],

        item["opportunity_score"]

    )

    print(

        family,

        "|",

        score

    )