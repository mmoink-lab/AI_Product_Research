from database.market_repository import MarketRepository
from database.product_score_repository import ProductScoreRepository

from intelligence.top_selling_engine import TopSellingEngine
from intelligence.family_price_analyzer import FamilyPriceAnalyzer
from intelligence.opportunity_engine import OpportunityEngine
from intelligence.evergreen_engine import EvergreenEngine
from intelligence.seasonal_engine import SeasonalEngine


repo = MarketRepository()

products = repo.load_products()


top = TopSellingEngine().analyze(products)

price = FamilyPriceAnalyzer().analyze(products)

price_map = {}

for p in price:

    price_map[p["family"]] = p


score_repo = ProductScoreRepository()

ever = EvergreenEngine()

season = SeasonalEngine()

opp = OpportunityEngine()


for item in top:

    family = item["family"]

    avg_price = price_map[family]["average"]

    opportunity = opp.calculate(
        item["score"],
        avg_price
    )

    score_repo.update_scores(

        family,

        item["score"],

        ever.calculate(family),

        season.calculate(family),

        opportunity

    )

print("All Scores Saved.")