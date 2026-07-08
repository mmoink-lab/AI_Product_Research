from core.pipeline import ProductPipeline
from research.price_intelligence import PriceIntelligence

pipeline = ProductPipeline()

engine = PriceIntelligence()

products = [

    {"product_name": "Mini USB Blender", "price": 850},
    {"product_name": "Portable Blender", "price": 990},
    {"product_name": "Rechargeable Blender", "price": 1200},

    {"product_name": "Bluetooth Ear Buds", "price": 750},
    {"product_name": "Wireless Earbuds", "price": 990},
    {"product_name": "Earbuds Pro", "price": 1350},

    {"product_name": "Vacuum Flask", "price": 450},
    {"product_name": "Thermal Water Bottle", "price": 780}

]

processed = pipeline.process(products)

report = engine.analyze(processed)

print("=" * 100)

for fp, info in report.items():

    print(fp)

    print(info)

    print()

print("=" * 100)