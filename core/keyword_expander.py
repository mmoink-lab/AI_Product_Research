class KeywordExpander:

    KEYWORDS = {

        "Mini Blender": [

            "mini blender",
            "portable blender",
            "usb blender",
            "smoothie blender",
            "juice blender",
            "personal blender",
            "fruit blender",
            "shake blender",
            "juice cup",
            "portable juicer",
            "rechargeable blender"

        ],

        "Electric Grinder": [

            "electric grinder",
            "coffee grinder",
            "spice grinder",
            "masala grinder",
            "powder grinder",
            "grain grinder",
            "dry grinder",
            "herb grinder",
            "seed grinder",
            "bean grinder"

        ],

        "Vegetable Chopper": [

            "vegetable chopper",
            "food chopper",
            "garlic chopper",
            "onion chopper",
            "vegetable cutter",
            "food cutter",
            "manual chopper"

        ],

        "Spin Mop": [

            "spin mop",
            "magic mop",
            "360 mop"

        ],

        "LED Strip Light": [

            "led strip light",
            "rgb led strip",
            "rgb strip light",
            "led light strip"

        ]

    }

    @classmethod
    def expand(cls, keyword):

        keyword = keyword.lower().strip()

        for family, keywords in cls.KEYWORDS.items():

            for item in keywords:

                if keyword == item.lower():

                    return keywords

        return [keyword]