from research.daraz_scraper import DarazResearch
from core.keyword_expander import KeywordExpander


class MarketResearch:

    def __init__(self):

        self.scrapers = [

            DarazResearch()

        ]

    def search(self, keyword):

        search_keywords = KeywordExpander.expand(keyword)

        all_products = []

        seen = set()

        print()
        print("Search Keywords")
        print("-" * 60)

        for k in search_keywords:

            print(">", k)

        print("-" * 60)

        for search_keyword in search_keywords:

            for scraper in self.scrapers:

                try:

                    products = scraper.search(search_keyword)

                except Exception:

                    continue

                for item in products:

                    name = item["product"].strip().lower()

                    if name in seen:

                        continue

                    seen.add(name)

                    all_products.append(item)

        return all_products

    def close(self):

        for scraper in self.scrapers:

            try:

                scraper.close()

            except Exception:

                pass