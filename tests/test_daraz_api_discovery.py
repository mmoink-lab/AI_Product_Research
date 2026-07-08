from research.market_sources.daraz import DarazProvider

provider = DarazProvider()

html = provider.download("usb blender")

keywords = [
    "mtop",
    "api",
    "graphql",
    "search",
    "catalog",
    "pcSearch",
    "lazada",
    "window.__",
    "__INIT_DATA__",
    "__data__",
]

print("=" * 80)

for key in keywords:

    if key.lower() in html.lower():

        print(f"FOUND : {key}")

print("=" * 80)