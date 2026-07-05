from research.daraz_scraper import DarazResearch
from intelligence.market_price import MarketPriceAnalyzer


bot = DarazResearch()

products = bot.search("Mini Blender")

bot.close()

analyzer = MarketPriceAnalyzer()

result = analyzer.analyze(products)

print(result)