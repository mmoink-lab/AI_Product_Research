from core.feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

products = [

    "USB Mini Blender 380ML Rechargeable",

    "Electric Spice Grinder 1500W Stainless Steel",

    "Portable Vegetable Chopper 900ML",

    "Magic Spin Mop Stainless Steel",

    "RGB LED Strip Light 5 Meter"

]

for product in products:

    print("=" * 60)

    print(product)

    print(extractor.extract(product))