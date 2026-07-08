"""
Market Analyzer v1
"""

import re
from collections import Counter


class MarketAnalyzer:

    def __init__(self):

        self.colors = {
            "black", "white", "red", "green", "blue",
            "yellow", "pink", "purple", "silver",
            "gold", "grey", "gray", "orange", "brown"
        }

    def extract_sizes(self, text):

        text = text.lower()

        pattern = r"\d+(?:\.\d+)?\s?(ml|l|kg|g|gm|cm|mm|inch)"

        return re.findall(pattern, text)

    def extract_colors(self, text):

        text = text.lower()

        result = []

        for color in self.colors:

            if color in text:
                result.append(color)

        return result

    def analyze(self, products):

        groups = {}

        for product in products:

            fp = product["fingerprint"]

            groups.setdefault(fp, []).append(product)

        report = {}

        for fp, items in groups.items():

            keyword_counter = Counter()

            color_counter = Counter()

            size_counter = Counter()

            for item in items:

                words = re.findall(
                    r"[a-zA-Z]+",
                    item["product_name"].lower()
                )

                keyword_counter.update(words)

                color_counter.update(
                    self.extract_colors(
                        item["product_name"]
                    )
                )

                size_counter.update(
                    self.extract_sizes(
                        item["product_name"]
                    )
                )

            report[fp] = {

                "fingerprint": fp,

                "total_products": len(items),

                "unique_keywords": len(keyword_counter),

                "top_keywords": keyword_counter.most_common(10),

                "colors": color_counter.most_common(),

                "sizes": size_counter.most_common()

            }

        return report