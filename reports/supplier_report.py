from research.daraz_scraper import DarazResearch
from intelligence.bd_market_engine import BDMarketEngine
from intelligence.market_decision import MarketDecision


supplier = "USB Mini Blender 380ML Rechargeable"

research = DarazResearch()

market = research.search("Mini Blender")

research.close()

engine = BDMarketEngine()

decision = MarketDecision()

results = engine.analyze(
    supplier,
    market
)

best = results[0]

print("=" * 80)

print("Supplier Product")
print(supplier)

print("=" * 80)

print("Best Bangladesh Match")

print(best["product"])

print()

print("Price :", best["price"])

print("Score :", best["score"])

print("Decision :", decision.evaluate(best["score"]))

print("=" * 80)