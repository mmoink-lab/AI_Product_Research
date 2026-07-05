from research.daraz_scraper import DarazResearch
from intelligence.relevance import RelevanceAnalyzer


research = DarazResearch()

products = research.search("Mini Blender")

research.close()

analyzer = RelevanceAnalyzer()

for item in products:

    score = analyzer.score(
        "Mini Blender",
        item["product"]
    )

    print(score, item["product"])