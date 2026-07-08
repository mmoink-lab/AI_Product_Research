"""
Product Fingerprint Engine v2
"""

import re


class ProductFingerprint:

    def __init__(self):

        self.stop_words = {
            "new", "original", "best", "premium", "quality",
            "portable", "mini", "wireless", "rechargeable",
            "smart", "digital", "electric", "automatic",
            "usb", "led", "pcs", "pc", "set", "pack",
            "piece", "pieces", "latest", "official",
            "genuine", "fast"
        }

        self.colors = {
            "black", "white", "red", "green", "blue",
            "yellow", "pink", "purple", "silver",
            "gold", "grey", "gray", "orange", "brown"
        }

        self.units = {
            "ml", "l", "kg", "g", "gm",
            "cm", "mm", "inch", "ft", "meter",
            "w", "mah"
        }

        self.priority = [
            "blender",
            "earbuds",
            "flask",
            "bottle",
            "charger",
            "cable",
            "speaker",
            "fan",
            "watch",
            "tripod",
            "camera",
            "mouse",
            "keyboard",
            "powerbank",
            "lamp"
        ]

        self.synonyms = {

            "ear": "earbuds",
            "buds": "earbuds",
            "earbud": "earbuds",

            "smoothie": "blender",
            "fruit": "blender",
            "juice": "blender",
            "juicer": "blender",

            "thermal": "flask",
            "vacuum": "flask",

            "feeding": "baby",
            "milk": "baby",

            "charge": "charger",
            "charging": "charger",

            "typec": "cable",
            "type": "cable"

        }

    def clean(self, text):

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

        merged = []

        i = 0

        while i < len(words):

            if (
                i + 1 < len(words)
                and words[i] == "earbuds"
                and words[i + 1] == "earbuds"
            ):
                merged.append("earbuds")
                i += 2
                continue

            merged.append(words[i])
            i += 1

        result = []

        for word in merged:

            if word not in result:
                result.append(word)

        return result

    def fingerprint(self, product_name):

        words = self.clean(product_name)

        for keyword in self.priority:

            if keyword in words:
                return keyword

        if not words:
            return "unknown"

        return words[0]

    def fingerprint_details(self, product_name):

        words = self.clean(product_name)

        return {
            "original": product_name,
            "fingerprint": self.fingerprint(product_name),
            "keywords": words
        }