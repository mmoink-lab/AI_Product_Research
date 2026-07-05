from database.market_repository import MarketRepository

from intelligence.demand_engine import DemandEngine
from intelligence.competition_engine import CompetitionEngine
from intelligence.saturation_engine import SaturationEngine
from intelligence.evergreen_engine import EvergreenEngine
from intelligence.seasonal_engine import SeasonalEngine
from intelligence.price_engine import PriceEngine
from intelligence.final_ranking_engine import FinalRankingEngine
from intelligence.product_decision import ProductDecision


products = MarketRepository().load_products()

demand_engine = DemandEngine()

competition_engine = CompetitionEngine()

saturation_engine = SaturationEngine()

evergreen_engine = EvergreenEngine()

seasonal_engine = SeasonalEngine()

price_engine = PriceEngine()

ranking_engine = FinalRankingEngine()

decision_engine = ProductDecision()


demand = {

    item["family"]: item

    for item in demand_engine.analyze(products)

}

competition = {

    item["family"]: item

    for item in competition_engine.analyze(products)

}

saturation = {

    item["family"]: item

    for item in saturation_engine.analyze(products)

}

prices = {

    item["family"]: item

    for item in price_engine.analyze(products)

}


families = {}

for item in products:

    families[item["family"]] = item


print("=" * 110)

print("BANGLADESH PRODUCT INTELLIGENCE REPORT")

print("=" * 110)


for family in sorted(families):

    d = demand.get(family, {})

    c = competition.get(family, {})

    s = saturation.get(family, {})

    p = prices.get(family, {})

    evergreen = evergreen_engine.calculate(

        family

    )

    seasonal = seasonal_engine.calculate(

        family

    )

    score = ranking_engine.calculate(

        d.get("demand", 0),

        c.get("competition_score", 0),

        s.get("saturation_score", 0),

        evergreen,

        seasonal

    )

    print()

    print("=" * 110)

    print("Product Family")

    print()

    print(family)

    print()

    print("Overall Rating")

    if score >= 80:

        stars = "⭐⭐⭐⭐⭐"

    elif score >= 70:

        stars = "⭐⭐⭐⭐"

    elif score >= 60:

        stars = "⭐⭐⭐"

    elif score >= 50:

        stars = "⭐⭐"

    else:

        stars = "⭐"

    print(stars)

    print()

    print("Market Status")

    print()

    print(decision_engine.get(score))

    print()

    print("-" * 60)

    print("Market Statistics")

    print()

    print(f"Listings              : {d.get('listings',0)}")

    print(f"Total Sold            : {d.get('sold',0)}")

    print(f"Demand Score          : {round(d.get('demand',0),2)}")

    print(f"Competition Score     : {c.get('competition_score',0)}")

    print(f"Saturation Score      : {s.get('saturation_score',0)}")

    print(f"Evergreen Score       : {evergreen}")

    print(f"Seasonal Score        : {seasonal}")

    print()

    print("-" * 60)

    print("Price Analysis")

    print()

    print(f"Lowest Price          : {p.get('lowest',0)} Tk")

    print(f"Average Price         : {p.get('average',0)} Tk")

    print(f"Median Price          : {p.get('median',0)} Tk")

    print(f"Highest Price         : {p.get('highest',0)} Tk")

    print(f"Market Segment        : {p.get('segment','')}")

    print()

    print("-" * 60)

    print("Final Intelligence")

    print()

    print(f"Final Score           : {round(score,2)}")

    print(f"Recommendation        : {decision_engine.get(score)}")

print()

print("=" * 110)