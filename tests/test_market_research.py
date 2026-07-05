from research.market_research import MarketResearch

research = MarketResearch()

products = research.search("mini blender")

research.close()

print("=" * 70)

print("Products:", len(products))

print()

for item in products[:10]:

    print(item)