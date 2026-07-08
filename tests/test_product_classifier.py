from intelligence.product_classifier import ProductClassifier

engine = ProductClassifier()

products = [

    "Mini USB Blender 350ml",

    "Portable Smoothie Blender",

    "Bluetooth Ear Buds",

    "Vacuum Flask",

    "Thermal Water Bottle",

    "Fast Charger 33W",

    "Type C Cable",

    "Gaming Mouse",

    "RGB Keyboard",

    "LED Study Lamp"

]

print("=" * 100)

for product in products:

    print(engine.classify(product))

print("=" * 100)