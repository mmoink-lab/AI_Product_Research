import re


class FeatureExtractor:

    PRODUCT_TYPES = [
        "blender",
        "grinder",
        "chopper",
        "mop",
        "strip light",
        "fan",
        "speaker",
        "tripod",
        "kettle",
        "humidifier",
        "vacuum"
    ]

    FEATURES = [
        "usb",
        "rechargeable",
        "portable",
        "electric",
        "wireless",
        "stainless steel",
        "foldable",
        "automatic",
        "manual",
        "mini"
    ]

    def extract(self, product_name):

        text = product_name.lower()

        text = re.sub(r"\s+", " ", text)

        data = {
            "product_type": None,
            "features": [],
            "capacity": None,
            "power": None
        }

        for item in self.PRODUCT_TYPES:

            if item in text:
                data["product_type"] = item
                break

        for feature in self.FEATURES:

            if feature in text:
                data["features"].append(feature)

        capacity = re.search(r"(\d+)\s?(ml|l)", text)

        if capacity:
            data["capacity"] = capacity.group()

        power = re.search(r"(\d+)\s?(w|watt)", text)

        if power:
            data["power"] = power.group()

        return data