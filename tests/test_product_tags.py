from intelligence.product_tags import ProductTags

families = [

    "Mini Blender",

    "Electric Grinder",

    "LED Strip Light",

    "Spin Mop"

]

for family in families:

    print("=" * 60)

    print(family)

    print(ProductTags.get(family))