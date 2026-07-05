class OpportunityEngine:

    def calculate(

        self,

        demand,

        market_strength,

        saturation,

        evergreen,

        seasonal

    ):

        score = (

            demand * 0.30 +

            market_strength * 0.25 +

            saturation * 0.20 +

            evergreen * 0.15 +

            seasonal * 0.10

        )

        return round(score, 2)