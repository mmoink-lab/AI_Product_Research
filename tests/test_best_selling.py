from research.daraz_scraper import DarazResearch
from intelligence.family_detector import ProductFamilyDetector
from intelligence.best_selling import BestSellingAnalyzer


research = DarazResearch()

products = research.search("Mini Blender")

research.close()

detector = ProductFamilyDetector()

dataset = []

for item in products:

    dataset.append({

        "family": detector.detect(item["product"])

    })

analyzer = BestSellingAnalyzer()

result = analyzer.analyze(dataset)

for row in result:

    print(row)