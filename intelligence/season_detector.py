from datetime import datetime


class SeasonDetector:

    def current_season(self):

        month = datetime.now().month

        if month in [12, 1]:
            return "winter"

        elif month in [2, 3, 4]:
            return "summer"

        elif month in [5, 6]:
            return "rainy"

        elif month in [7, 8]:
            return "monsoon"

        elif month in [9, 10]:
            return "autumn"

        else:
            return "late_autumn"