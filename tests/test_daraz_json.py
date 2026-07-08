from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

html = provider.download("usb blender")

keywords = [

    "__NEXT_DATA__",
    "__NUXT__",
    "mods",
    "products",
    "productItems",
    "catalog",
    "searchItems"

]

print("=" * 80)

for key in keywords:

    print(key, ":", key in html)

print("=" * 80)