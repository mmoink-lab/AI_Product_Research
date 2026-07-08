"""
Product Classifier v1
"""

from intelligence.product_fingerprint import ProductFingerprint


class ProductClassifier:

    def __init__(self):

        self.fp = ProductFingerprint()

        self.categories = {

            "blender": (
                "Home & Kitchen",
                "Kitchen Appliances",
                "Blender"
            ),

            "earbuds": (
                "Electronics",
                "Audio",
                "Wireless Earbuds"
            ),

            "flask": (
                "Home & Kitchen",
                "Drinkware",
                "Vacuum Flask"
            ),

            "bottle": (
                "Baby & Kids",
                "Feeding",
                "Baby Bottle"
            ),

            "charger": (
                "Electronics",
                "Mobile Accessories",
                "Charger"
            ),

            "cable": (
                "Electronics",
                "Mobile Accessories",
                "Cable"
            ),

            "speaker": (
                "Electronics",
                "Audio",
                "Speaker"
            ),

            "fan": (
                "Home Appliances",
                "Cooling",
                "Fan"
            ),

            "watch": (
                "Fashion",
                "Accessories",
                "Watch"
            ),

            "tripod": (
                "Electronics",
                "Photography",
                "Tripod"
            ),

            "camera": (
                "Electronics",
                "Photography",
                "Camera"
            ),

            "mouse": (
                "Computers",
                "Accessories",
                "Mouse"
            ),

            "keyboard": (
                "Computers",
                "Accessories",
                "Keyboard"
            ),

            "powerbank": (
                "Electronics",
                "Mobile Accessories",
                "Power Bank"
            ),

            "lamp": (
                "Home & Living",
                "Lighting",
                "Lamp"
            )

        }

    def classify(self, product_name):

        fingerprint = self.fp.fingerprint(product_name)

        category = self.categories.get(

            fingerprint,

            (
                "Unknown",
                "Unknown",
                "Unknown"
            )

        )

        return {

            "product_name": product_name,

            "fingerprint": fingerprint,

            "main_category": category[0],

            "sub_category": category[1],

            "product_type": category[2]

        }