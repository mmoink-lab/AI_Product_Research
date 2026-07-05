from core.product_normalizer import ProductNormalizer

samples = [

    "USB Mini Blender 380ML Rechargeable",

    "Portable USB Blender 380ml",

    "Mini Blender Original",

    "Mini Blender (New Version)",

    "Electric Coffee Grinder 1500W",

    "Coffee Grinder Stainless Steel",

    "Garlic Chopper Premium",

    "Vegetable Chopper Official"

]

print("=" * 80)

for item in samples:

    print(item)

    print("->", ProductNormalizer.normalize(item))

    print("-" * 80)