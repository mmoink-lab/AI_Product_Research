from intelligence.product_tags import ProductTags


class EvergreenEngine:

    def calculate(self, family):

        tags = ProductTags.get(family)

        if tags["evergreen"]:
            return 100

        return 40