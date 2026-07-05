from research.daraz_scraper import DarazResearch
from intelligence.similarity_engine import SimilarityEngine


research = DarazResearch()

products = research.search("Mini Blender")

research.close()

engine = SimilarityEngine()

for item in products:

    score = engine.score(
        "Mini Blender",
        item["product"]
    )

    print(
        f"{score:>6} | {item['price']:>5} | {item['product']}"
    )