from collections import Counter


class SaturationEngine:

    def analyze(self, products):

        families = []

        for item in products:

            family = item.get("family", "").strip()

            if family:

                families.append(family)

        counter = Counter(families)

        results = []

        for family, listings in counter.items():

            # Bangladesh market saturation scale
            if listings <= 10:

                score = 100

            elif listings <= 25:

                score = 80

            elif listings <= 50:

                score = 60

            elif listings <= 80:

                score = 40

            else:

                score = 20

            results.append({

                "family": family,

                "listings": listings,

                "saturation_score": score

            })

        return sorted(

            results,

            key=lambda x: x["saturation_score"],

            reverse=True

        )