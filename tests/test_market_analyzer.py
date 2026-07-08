from core.pipeline import ProductPipeline
from research.market_analyzer import MarketAnalyzer

pipeline = ProductPipeline()

engine = MarketAnalyzer()

products = [

    {
        "product_name": "Mini USB Blender 350ml Black",
        "price": 850
    },

    {
        "product_name": "Portable Blender 500ml White",
        "price": 990
    },

    {
        "product_name": "Rechargeable Smoothie Blender Red",
        "price": 1100
    },

    {
        "product_name": "Bluetooth Ear Buds Black",
        "price": 890
    },

    {
        "product_name": "Wireless Earbuds White",
        "price": 990
    }

]

processed = pipeline.process(products)

report = engine.analyze(processed)

from pprint import pprint

pprint(report)