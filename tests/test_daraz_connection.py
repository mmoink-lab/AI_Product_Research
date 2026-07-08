from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

html = provider.download("usb blender")

print("=" * 80)

print("Downloaded:", len(html), "characters")

print()

print(html[:500])

print()

print("=" * 80)