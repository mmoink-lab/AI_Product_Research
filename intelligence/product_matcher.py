from rapidfuzz import fuzz


class ProductMatcher:

    def match(self, supplier, market):

        score = 0

        # Product Type (40%)

        if supplier["product_type"] == market["product_type"]:
            score += 40

        # Features (30%)

        supplier_features = set(supplier["features"])
        market_features = set(market["features"])

        if supplier_features:

            matched = len(
                supplier_features & market_features
            )

            score += (matched / len(supplier_features)) * 30

        # Capacity (15%)

        if (
            supplier["capacity"]
            and supplier["capacity"] == market["capacity"]
        ):
            score += 15

        # Power (15%)

        if (
            supplier["power"]
            and supplier["power"] == market["power"]
        ):
            score += 15

        return round(score, 2)

    def fuzzy_score(self, supplier_name, market_name):

        return round(
            fuzz.token_sort_ratio(
                supplier_name.lower(),
                market_name.lower()
            ),
            2
        )