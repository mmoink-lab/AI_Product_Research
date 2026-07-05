from collections import defaultdict


class CompetitionEngine:

    def analyze(self, products):

        families = defaultdict(

            lambda: {

                "listings": 0,

                "sold": 0

            }

        )

        for item in products:

            family = item.get("family", "").strip()

            if not family:
                continue

            families[family]["listings"] += 1

            families[family]["sold"] += item.get(

                "sold_count",

                0

            )

        results = []

        for family, data in families.items():

            listings = data["listings"]

            sold = data["sold"]

            ratio = sold / listings if listings else 0

            if ratio >= 150:

                score = 100

            elif ratio >= 100:

                score = 90

            elif ratio >= 70:

                score = 80

            elif ratio >= 40:

                score = 60

            elif ratio >= 20:

                score = 40

            else:

                score = 20

            results.append({

                "family": family,

                "listings": listings,

                "sold": sold,

                "ratio": round(ratio, 2),

                "competition_score": score

            })

        return sorted(

            results,

            key=lambda x: x["competition_score"],

            reverse=True

        )