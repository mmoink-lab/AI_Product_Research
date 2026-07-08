from pprint import pprint

from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

products = provider.search("usb blender")

print("=" * 100)

print("Products:", len(products))

print()

for item in products[:10]:

    pprint(item)

    print()

print("=" * 100)