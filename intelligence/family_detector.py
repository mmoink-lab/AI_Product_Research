import re


class ProductFamilyDetector:

    KEYWORDS = {
        "Mini Blender": [
            "portable usb blender",
            "portable blender",
            "usb blender",
            "mini blender",
            "juicer blender",
            "blender"
        ],

        "Vegetable Chopper": [
            "vegetable chopper",
            "electric chopper",
            "food chopper",
            "garlic chopper",
            "mini chopper",
            "chopper"
        ],

        "Electric Grinder": [
            "electric grinder",
            "spice grinder",
            "coffee grinder",
            "mini grinder",
            "grinder"
        ],

        "LED Strip Light": [
            "led strip light",
            "led strip",
            "strip light",
            "rgb light"
        ],

        "Spin Mop": [
            "magic spin mop",
            "spin mop",
            "magic mop"
        ]
    }

    def detect(self, product_name):

        text = product_name.lower()
        text = re.sub(r"[^a-z0-9 ]", " ", text)

        scores = {}

        for family, keywords in self.KEYWORDS.items():

            score = 0

            for keyword in keywords:

                if keyword in text:
                    score += len(keyword)

            if score > 0:
                scores[family] = score

        if not scores:
            return "Others"

        return max(scores, key=scores.get)