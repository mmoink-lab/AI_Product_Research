from research.datasource import DataSource

ds = DataSource()

products = [

    {
        "name": "Mini USB Blender",
        "fingerprint": "blender",
        "price": 850
    },

    {
        "name": "Portable Blender",
        "fingerprint": "blender",
        "price": 990
    },

    {
        "name": "Rechargeable Blender",
        "fingerprint": "blender",
        "price": 1150
    },

    {
        "name": "Bluetooth Earbuds",
        "fingerprint": "earbuds",
        "price": 680
    },

    {
        "name": "Wireless Earbuds",
        "fingerprint": "earbuds",
        "price": 920
    }

]

ds.load(products)

print("=" * 80)

print("Total Products :", ds.total_products())

print("Unique Families :", ds.unique_families())

print("Average Blender Price :", ds.average_price("blender"))

print("Lowest Blender Price :", ds.lowest_price("blender"))

print("Highest Blender Price :", ds.highest_price("blender"))

print()

print(ds.filter_by_fingerprint("earbuds"))

print("=" * 80)