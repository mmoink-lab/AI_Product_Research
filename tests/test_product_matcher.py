from core.feature_extractor import FeatureExtractor
from intelligence.product_matcher import ProductMatcher


extractor = FeatureExtractor()

matcher = ProductMatcher()


supplier = extractor.extract(
    "USB Mini Blender 380ML Rechargeable"
)

market = extractor.extract(
    "Portable USB Blender 380ML Rechargeable"
)

score = matcher.match(
    supplier,
    market
)

fuzzy = matcher.fuzzy_score(
    "USB Mini Blender 380ML Rechargeable",
    "Portable USB Blender 380ML Rechargeable"
)

print("Feature Score :", score)
print("Name Score    :", fuzzy)