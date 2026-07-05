from research.daraz_scraper import DarazResearch
from intelligence.bd_market_engine import BDMarketEngine

supplier = "USB Mini Blender 380ML Rechargeable"

research = DarazResearch()

market = research.search("Mini Blender")

print("Search Result Count:", len(market))

if market:
    print("First Product:", market[0])

engine = BDMarketEngine()

results = engine.analyze(
    supplier,
    market
)

research.close()

print("Final Result Count:", len(results))

print("=" * 100)

for item in results[:10]:
    print(item)