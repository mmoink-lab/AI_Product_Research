class ProductTags:

    TAGS = {

        "Mini Blender": {
            "evergreen": True,
            "summer": True,
            "winter": False,
            "ramadan": True,
            "eid": False
        },

        "Electric Grinder": {
            "evergreen": True,
            "summer": False,
            "winter": False,
            "ramadan": True,
            "eid": True
        },

        "Vegetable Chopper": {
            "evergreen": True,
            "summer": False,
            "winter": False,
            "ramadan": True,
            "eid": True
        },

        "LED Strip Light": {
            "evergreen": False,
            "summer": False,
            "winter": False,
            "ramadan": False,
            "eid": True
        },

        "Spin Mop": {
            "evergreen": True,
            "summer": False,
            "winter": False,
            "ramadan": False,
            "eid": False
        }

    }

    @classmethod
    def get(cls, family):

        return cls.TAGS.get(
            family,
            {
                "evergreen": False,
                "summer": False,
                "winter": False,
                "ramadan": False,
                "eid": False
            }
        )