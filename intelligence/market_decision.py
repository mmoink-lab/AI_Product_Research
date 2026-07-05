class MarketDecision:

    def evaluate(self, score):

        if score >= 85:
            return "Excellent Opportunity"

        if score >= 70:
            return "Good Opportunity"

        if score >= 55:
            return "Average Opportunity"

        return "Poor Opportunity"