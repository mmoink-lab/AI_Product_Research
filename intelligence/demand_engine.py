from collections import defaultdict


class DemandEngine:

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

        highest_sold = max(

            (

                data["sold"]

                for data in families.values()

            ),

            default=1

        )

        highest_avg = max(

            (

                data["sold"] / data["listings"]

                for data in families.values()

                if data["listings"]

            ),

            default=1

        )

        results = []

        for family, data in families.items():

            listings = data["listings"]

            sold = data["sold"]

            avg = sold / listings if listings else 0

            sold_score = (

                sold / highest_sold

            ) * 100

            avg_score = (

                avg / highest_avg

            ) * 100

            demand = (

                sold_score * 0.70 +

                avg_score * 0.30

            )

            results.append({

                "family": family,

                "listings": listings,

                "sold": sold,

                "average_sold": round(avg, 2),

                "demand": round(demand, 2)

            })

        return sorted(

            results,

            key=lambda x: x["demand"],

            reverse=True

        )