from intelligence.product_fingerprint import ProductFingerprint

engine = ProductFingerprint()

products = [

    "Mini USB Blender 350ml",

    "Portable Smoothie Blender",

    "Fruit Juicer Blender",

    "Rechargeable Blender",

    "Wireless Earbuds",

    "Bluetooth Ear Buds",

    "Baby Feeding Bottle",

    "Baby Milk Bottle",

    "Vacuum Flask",

    "Thermal Water Bottle",

    "Fast Charger 33W",

    "Type C Cable"

]

print("=" * 80)

for product in products:

    data = engine.fingerprint_details(product)

    print(data)

print("=" * 80)