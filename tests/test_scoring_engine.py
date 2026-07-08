from intelligence.scoring_engine import ProductScoringEngine

engine = ProductScoringEngine()

products = [

    "blender",

    "earbuds",

    "charger",

    "flask",

    "lamp",

    "keyboard",

    "camera"

]

print("=" * 100)

for product in products:

    print(engine.analyze(product))

print("=" * 100)