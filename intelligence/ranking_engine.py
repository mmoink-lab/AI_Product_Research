"""
Ranking Engine
Production v1
"""


class RankingEngine:

    def calculate(self, products):

        ranked = []

        for item in products:

            demand = item.get("demand_score", 0)

            competition = item.get("competition_score", 0)

            profit = item.get("profit_score", 0)

            shipping = item.get("shipping_score", 0)

            score = round(

                demand * 0.35 +

                profit * 0.30 +

                shipping * 0.20 +

                (100 - competition) * 0.15

            )

            row = dict(item)

            row["winner_score"] = score

            ranked.append(row)

        ranked.sort(

            key=lambda x: x["winner_score"],

            reverse=True

        )

        return ranked