class FinalMatchScore:

    def calculate(
        self,
        feature_score,
        name_score,
        position,
        total_results
    ):

        # Feature Match (50%)
        feature = feature_score * 0.50

        # Name Similarity (30%)
        name = name_score * 0.30

        # Search Position (20%)
        if total_results <= 1:
            position_score = 100
        else:
            position_score = (
                (total_results - position)
                / (total_results - 1)
            ) * 100

        position = position_score * 0.20

        return round(
            feature + name + position,
            2
        )