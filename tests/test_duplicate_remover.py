from core.duplicate_remover import DuplicateRemover

products = [

    {

        "product": "USB Mini Blender 380ML Rechargeable",

        "price": 850,

        "sold_count": 25

    },

    {

        "product": "USB Mini Blender",

        "price": 890,

        "sold_count": 91

    },

    {

        "product": "Mini Blender Original",

        "price": 820,

        "sold_count": 18

    },

    {

        "product": "Coffee Grinder 1500W",

        "price": 1200,

        "sold_count": 50

    },

    {

        "product": "Coffee Grinder Stainless Steel",

        "price": 1180,

        "sold_count": 82

    }

]

results = DuplicateRemover.remove(

    products

)

print("=" * 80)

print("Before :", len(products))

print("After  :", len(results))

print("=" * 80)

for item in results:

    print(

        item["normalized_name"],

        "|",

        item["sold_count"],

        "|",

        item["product"]

    )