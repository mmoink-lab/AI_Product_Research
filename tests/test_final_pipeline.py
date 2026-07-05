from database.market_repository import MarketRepository

from intelligence.demand_engine import DemandEngine
from intelligence.competition_engine import CompetitionEngine
from intelligence.saturation_engine import SaturationEngine
from intelligence.evergreen_engine import EvergreenEngine
from intelligence.seasonal_engine import SeasonalEngine
from intelligence.final_ranking_engine import FinalRankingEngine
from intelligence.product_decision import ProductDecision


repo = MarketRepository()

products = repo.load_products()

demand_engine = DemandEngine()
competition_engine = CompetitionEngine()
saturation_engine = SaturationEngine()
evergreen_engine = EvergreenEngine()
seasonal_engine = SeasonalEngine()

rank_engine = FinalRankingEngine()

decision = ProductDecision()

demand = {}

for item in demand_engine.analyze(products):

    demand[item["family"]] = item["demand"]

competition = {}

for item in competition_engine.analyze(products):

    competition[item["family"]] = item["competition_score"]

saturation = {}

for item in saturation_engine.analyze(products):

    saturation[item["family"]] = item["saturation_score"]

families = {}

for item in products:

    family = item["family"]

    if family and family not in families:

        families[family] = item

print("=" * 100)

print("BD PRODUCT INTELLIGENCE")

print("=" * 100)

for family in families:

    evergreen = evergreen_engine.calculate(family)

    seasonal = seasonal_engine.calculate(family)

    final_score = rank_engine.calculate(

        demand.get(family, 0),

        competition.get(family, 0),

        saturation.get(family, 0),

        evergreen,

        seasonal

    )

    print()

    print("Family          :", family)

    print("Demand          :", demand.get(family, 0))

    print("Competition     :", competition.get(family, 0))

    print("Saturation      :", saturation.get(family, 0))

    print("Evergreen       :", evergreen)

    print("Seasonal        :", seasonal)

    print("Final Score     :", final_score)

    print("Recommendation  :", decision.get(final_score))

    print("-" * 100)