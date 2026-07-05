class AIRankingEngine:

    def calculate(
        self,
        top_selling,
        evergreen,
        seasonal,
        competition
    ):

        # ?? Competition = ???? Score
        competition_score = 100 - competition

        score = (

            top_selling * 0.35 +

            evergreen * 0.25 +

            seasonal * 0.20 +

            competition_score * 0.20

        )

        return round(score, 2)