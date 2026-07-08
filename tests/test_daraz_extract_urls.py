import re

from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

html = provider.download("usb blender")

patterns = [
    r'https://[^"\']+',
    r'/api/[^"\']+',
    r'/catalog/[^"\']+',
    r'pcSearch[^"\']*',
    r'mtop[^"\']*',
]

found = set()

for pattern in patterns:

    for match in re.findall(pattern, html):

        found.add(match)

print("=" * 100)

for item in sorted(found):

    print(item)

print("=" * 100)