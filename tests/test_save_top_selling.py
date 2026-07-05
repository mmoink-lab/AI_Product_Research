from database.market_repository import MarketRepository
from database.product_score_repository import ProductScoreRepository

from intelligence.top_selling_engine import TopSellingEngine

repo = MarketRepository()

products = repo.load_products()

engine = TopSellingEngine()

results = engine.analyze(products)

score_repo = ProductScoreRepository()

for item in results:

    score_repo.update_top_selling(

        item["family"],
        item["top_selling_score"]

    )

print("Top Selling Score Saved Successfully")