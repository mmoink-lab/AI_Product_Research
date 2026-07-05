class ProductDecision:

    def get(self, score):

        if score >= 90:

            return "WINNER ⭐⭐⭐⭐⭐"

        elif score >= 75:

            return "HIGH POTENTIAL ⭐⭐⭐⭐"

        elif score >= 60:

            return "GOOD ⭐⭐⭐"

        elif score >= 45:

            return "WATCHLIST ⭐⭐"

        return "AVOID ⭐"