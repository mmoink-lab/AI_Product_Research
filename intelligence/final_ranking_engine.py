class FinalRankingEngine:

    def calculate(

        self,

        demand,

        market_strength,

        saturation,

        evergreen,

        seasonal

    ):

        score = (

            demand * 0.40 +

            market_strength * 0.25 +

            saturation * 0.15 +

            evergreen * 0.10 +

            seasonal * 0.10

        )

        return round(score, 2)