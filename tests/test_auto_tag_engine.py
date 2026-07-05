from core.feature_extractor import FeatureExtractor
from intelligence.auto_tag_engine import AutoTagEngine

products = [

    "USB Mini Blender 380ML Rechargeable",

    "Electric Spice Grinder 1500W Stainless Steel",

    "Portable Vegetable Chopper 900ML",

    "Magic Spin Mop Stainless Steel",

    "RGB LED Strip Light 5 Meter"

]

extractor = FeatureExtractor()
engine = AutoTagEngine()

for product in products:

    features = extractor.extract(product)

    tags = engine.generate(features)

    print("=" * 70)
    print(product)
    print(tags)