from intelligence.product_tags import ProductTags
from intelligence.season_detector import SeasonDetector


class SeasonalEngine:

    def __init__(self):

        self.detector = SeasonDetector()

    def calculate(self, family):

        tags = ProductTags.get(family)

        season = self.detector.current_season()

        score = 40

        if season == "summer" and tags["summer"]:
            score += 40

        if season == "winter" and tags["winter"]:
            score += 40

        return min(score, 100)