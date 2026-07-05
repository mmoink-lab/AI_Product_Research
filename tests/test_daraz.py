from research.daraz_scraper import DarazResearch

bot = DarazResearch()

results = bot.search("Mini Blender")

for item in results:
    print(item)

bot.close()