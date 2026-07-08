from intelligence.family_engine import ProductFamilyEngine

engine = ProductFamilyEngine()

products = [
    "Mini USB Blender 350ml",
    "Portable USB Blender",
    "Rechargeable Blender",
    "Fruit Juicer Blender",
    "Smoothie Blender",
    "Wireless Earbuds",
    "Bluetooth Ear Buds",
    "Earbuds Pro",
    "Baby Feeding Bottle",
    "Baby Milk Bottle",
    "Vacuum Flask 500ml",
    "Thermal Water Bottle"
]

families = engine.group_products(products)

print("=" * 80)

for i, family in enumerate(families, start=1):

    print(f"\nFamily {i}")
    print("Family Name :", family["family_name"])

    for p in family["products"]:
        print("  -", p)

print("\n" + "=" * 80)
print("Total Families :", len(families))