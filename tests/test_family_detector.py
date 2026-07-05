from core.family_detector import ProductFamilyDetector

products = [

    "USB Mini Blender 380ML Rechargeable",

    "Portable Smoothie Maker",

    "Portable Juicer USB",

    "Capsule Cutter Blender",

    "Coffee Grinder 1500W",

    "Dry Spice Grinder",

    "Masala Grinder",

    "Inima Japan Electric Spice Grinder",

    "Silver Crest Coffee Grinder",

    "Mini Electric Coffee Grinder",

    "Garlic Chopper",

    "Vegetable Cutter",

    "Magic Spin Mop",

    "RGB LED Strip Light",

    "Random Unknown Product"

]

print("=" * 80)

for product in products:

    print(

        product,

        "->",

        ProductFamilyDetector.get_family_name(product)

    )