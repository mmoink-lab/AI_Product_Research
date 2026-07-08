"""
Product Scoring Engine v1
"""


class ProductScoringEngine:

    def __init__(self):

        self.high_demand = {
            "blender",
            "earbuds",
            "charger",
            "cable",
            "powerbank",
            "fan",
            "tripod",
            "lamp",
            "mouse",
            "keyboard"
        }

        self.low_competition = {
            "tripod",
            "lamp",
            "vacuum",
            "flask"
        }

        self.high_profit = {
            "blender",
            "earbuds",
            "tripod",
            "lamp",
            "watch",
            "speaker"
        }

        self.easy_shipping = {
            "earbuds",
            "charger",
            "cable",
            "watch",
            "mouse",
            "keyboard",
            "lamp"
        }

    def demand_score(self, fingerprint):

        if fingerprint in self.high_demand:
            return 90

        return 60

    def competition_score(self, fingerprint):

        if fingerprint in self.low_competition:
            return 30

        return 70

    def profit_score(self, fingerprint):

        if fingerprint in self.high_profit:
            return 90

        return 65

    def shipping_score(self, fingerprint):

        if fingerprint in self.easy_shipping:
            return 95

        return 70

    def winner_score(self, demand, competition, profit, shipping):

        score = (
            demand * 0.35 +
            (100 - competition) * 0.30 +
            profit * 0.25 +
            shipping * 0.10
        )

        return round(score)

    def analyze(self, fingerprint):

        demand = self.demand_score(fingerprint)

        competition = self.competition_score(fingerprint)

        profit = self.profit_score(fingerprint)

        shipping = self.shipping_score(fingerprint)

        winner = self.winner_score(
            demand,
            competition,
            profit,
            shipping
        )

        return {
            "fingerprint": fingerprint,
            "demand_score": demand,
            "competition_score": competition,
            "profit_score": profit,
            "shipping_score": shipping,
            "winner_score": winner
        }