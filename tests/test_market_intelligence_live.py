from pprint import pprint

from research.market_intelligence import MarketIntelligence

engine = MarketIntelligence()

for fp in [

    "blender",
    "earbuds",
    "charger"

]:

    print("=" * 100)

    pprint(engine.analyze(fp))