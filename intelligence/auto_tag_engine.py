class AutoTagEngine:

    def generate(self, features):

        tags = {

            "evergreen": False,
            "summer": False,
            "winter": False,
            "ramadan": False,
            "eid": False

        }

        product_type = (features.get("product_type") or "").lower()

        feature_list = [
            f.lower() for f in features.get("features", [])
        ]

        # Kitchen products
        if product_type in [

            "blender",
            "grinder",
            "chopper",
            "mop"

        ]:
            tags["evergreen"] = True

        # Summer products
        if (
            "usb" in feature_list
            or "rechargeable" in feature_list
            or product_type == "blender"
        ):
            tags["summer"] = True

        # Ramadan
        if product_type in [

            "blender",
            "grinder",
            "chopper"

        ]:
            tags["ramadan"] = True

        # Eid
        if product_type in [

            "grinder",
            "chopper",
            "strip light"

        ]:
            tags["eid"] = True

        # Winter
        if product_type in [

            "heater",
            "blanket"

        ]:
            tags["winter"] = True

        return tags