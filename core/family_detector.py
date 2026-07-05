import re


class ProductFamilyDetector:

    FAMILY_RULES = {

        "Mini Blender": [

            "blender",
            "mini blender",
            "portable blender",
            "usb blender",
            "smoothie",
            "smoothie maker",
            "juice blender",
            "juice cup",
            "juicer",
            "portable juicer",
            "personal blender",
            "capsule cutter",
            "mixer"

        ],

        "Electric Grinder": [

            "grinder",
            "coffee grinder",
            "spice grinder",
            "electric grinder",
            "powder grinder",
            "masala grinder",
            "grain grinder",
            "dry grinder",
            "mill",
            "milling"

        ],

        "Vegetable Chopper": [

            "vegetable chopper",
            "food chopper",
            "garlic chopper",
            "onion chopper",
            "meat chopper",
            "chopper",
            "vegetable cutter",
            "cutter"

        ],

        "Spin Mop": [

            "spin mop",
            "magic mop",
            "mop"

        ],

        "LED Strip Light": [

            "led strip",
            "rgb strip",
            "strip light",
            "led light"

        ]

    }

    CLEAN_PATTERNS = [

        r"\(.*?\)",

        r"\[[^\]]*\]",

        r"\b\d+\s*(ml|l|kg|gm|g|cm|mm|inch|in|m|w|watt)\b",

        r"\b\d+\b",

        r"[-_/]",

        r"\s+"

    ]

    @classmethod
    def clean(cls, text):

        text = text.lower()

        for pattern in cls.CLEAN_PATTERNS:

            text = re.sub(

                pattern,

                " ",

                text,

                flags=re.IGNORECASE

            )

        return text.strip()

    @classmethod
    def get_family_name(cls, product_name):

        if not product_name:

            return ""

        name = cls.clean(product_name)

        # Long keyword first
        for family, keywords in cls.FAMILY_RULES.items():

            keywords = sorted(

                keywords,

                key=len,

                reverse=True

            )

            for keyword in keywords:

                if keyword in name:

                    return family

        return "UNKNOWN"