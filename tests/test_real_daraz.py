from pprint import pprint

from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

products = provider.search("usb blender")

print("=" * 100)

print("Products:", len(products))

print()

for p in products[:10]:

    pprint(p)

    print()

print("=" * 100)