"""
Product Family Engine v3
"""

import re
from difflib import SequenceMatcher


class ProductFamilyEngine:

    def __init__(self):

        self.stop_words = {
            "new", "original", "best", "premium", "quality",
            "portable", "rechargeable", "wireless", "mini",
            "smart", "usb", "digital", "led",
            "pcs", "pc", "set", "pack",
            "piece", "pieces", "edition",
            "genuine", "official", "latest",
            "gift", "travel", "foldable",
            "electric", "automatic"
        }

        self.colors = {
            "black", "white", "red", "green", "blue",
            "yellow", "pink", "purple", "silver",
            "gold", "grey", "gray", "brown", "orange"
        }

        self.units = {
            "ml", "l", "kg", "g", "gm",
            "inch", "cm", "mm", "meter",
            "m", "ft"
        }

        self.synonyms = {

            "ear": "earbuds",
            "buds": "earbuds",
            "earbud": "earbuds",

            "juice": "juicer",
            "juicing": "juicer",

            "thermal": "flask",
            "vacuum": "flask",
            "vacuumflask": "flask",

            "feeding": "baby",
            "milk": "baby",

            "smoothie": "blender",
            "fruit": "blender",
        }

    def normalize(self, text):

        if not text:
            return ""

        text = str(text).lower()

        text = re.sub(r"\([^)]*\)", " ", text)

        text = re.sub(r"\d+(\.\d+)?", " ", text)

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        words = []

        for word in text.split():

            if word in self.stop_words:
                continue

            if word in self.colors:
                continue

            if word in self.units:
                continue

            if len(word) <= 1:
                continue

            if word in self.synonyms:
                word = self.synonyms[word]

            words.append(word)

        return " ".join(words)

    def tokenize(self, text):

        tokens = self.normalize(text).split()

        tokens = list(dict.fromkeys(tokens))

        tokens.sort()

        return tokens

    def similarity(self, a, b):

        return SequenceMatcher(None, a, b).ratio()

    def keyword_score(self, t1, t2):

        common = set(t1) & set(t2)

        return len(common)

    def same_family(self, p1, p2):

        t1 = self.tokenize(p1)
        t2 = self.tokenize(p2)

        common = self.keyword_score(t1, t2)

        if common >= 2:
            return True, 1.0

        score = self.similarity(
            " ".join(t1),
            " ".join(t2)
        )

        if score >= 0.72:
            return True, score

        return False, score

    def generate_family_name(self, product):

        tokens = self.tokenize(product)

        if not tokens:
            return "Unknown Product"

        priority = [
            "blender",
            "earbuds",
            "flask",
            "bottle",
            "baby",
            "fan",
            "lamp",
            "watch",
            "speaker",
            "tripod",
            "camera",
            "mouse",
            "keyboard"
        ]

        for p in priority:
            if p in tokens:
                tokens.remove(p)
                return (p + " " + " ".join(tokens)).strip().title()

        return " ".join(tokens).title()

    def group_products(self, products):

        families = []

        for product in products:

            matched = False

            for family in families:

                ok, _ = self.same_family(
                    product,
                    family["family_name"]
                )

                if ok:
                    family["products"].append(product)
                    matched = True
                    break

            if not matched:

                families.append({

                    "family_name": self.generate_family_name(product),

                    "products": [product]

                })

        return families