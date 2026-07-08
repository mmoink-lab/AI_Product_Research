from core.pipeline import ProductPipeline

pipeline = ProductPipeline()

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
    }

]

result = pipeline.process(products)

print("=" * 120)

for item in result:

    print(item)

print("=" * 120)