from database.market_repository import MarketRepository

from intelligence.ai_ranking_engine import AIRankingEngine
from intelligence.competition_engine import CompetitionEngine
from intelligence.seasonal_engine import SeasonalEngine
from intelligence.evergreen_engine import EvergreenEngine

products = MarketRepository().load_products()

competition = CompetitionEngine().analyze(products)

competition_map = {}

for item in competition:

    competition_map[item["family"]] = item["competition"]

season = SeasonalEngine()

evergreen = EvergreenEngine()

engine = AIRankingEngine()

families = {}

for item in products:

    family = item["family"]

    if family in families:
        continue

    families[family] = item

print("=" * 100)

for family, item in families.items():

    score = engine.calculate(

        item["top_selling_score"],

        evergreen.calculate(family),

        season.calculate(family),

        competition_map[family]

    )

    print(

        family,

        "|",

        round(score, 2)

    )