from research.product_research_engine import ProductResearchEngine

engine = ProductResearchEngine()

products = [

    {
        "product_name": "Mini USB Blender 350ml",
        "price": 950
    },

    {
        "product_name": "Portable Smoothie Blender",
        "price": 1100
    },

    {
        "product_name": "Bluetooth Ear Buds",
        "price": 890
    },

    {
        "product_name": "Vacuum Flask",
        "price": 650
    },

    {
        "product_name": "Fast Charger 33W",
        "price": 490
    },

    {
        "product_name": "RGB Keyboard",
        "price": 1250
    }

]

results = engine.top_winners(products)

print("=" * 120)

for i, item in enumerate(results, start=1):

    print(
        f"{i:02d}. "
        f"{item['product_name']} | "
        f"Winner: {item['winner_score']} | "
        f"{item['fingerprint']}"
    )

print("=" * 120)